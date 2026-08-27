from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Any
from orchestrator.contracts import CreativeJob
from orchestrator.registry import Registry
from orchestrator.router import CapabilityRouter
from services.character_sheet import CharacterSheetSpec, build_character_sheet_payload

app=FastAPI(title="NSP AI Studio API",version="0.2.0")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])


class JobRequest(BaseModel):
    intent:str=Field(min_length=1)
    capabilities:list[str]=Field(min_length=1)
    local_only:bool=False
    consent_granted:bool=False
    payload:dict[str,Any]={}


class CharacterSheetRequest(BaseModel):
    subject_name: str = Field(min_length=1)
    reference_labels: list[str] = Field(min_length=1, max_length=5)
    consent_granted: bool = False


@app.get("/health")
def health(): return {"status":"ok","service":"nsp-api"}


@app.post("/v1/jobs")
def create_job(request:JobRequest):
    job=CreativeJob(request.intent,tuple(request.capabilities),request.payload,request.local_only,request.consent_granted)
    try: provider=CapabilityRouter(Registry()).route(job)
    except Exception as exc: raise HTTPException(422,str(exc)) from exc
    return {"job_id":"local-"+str(abs(hash(request.intent))),"status":"queued","provider":provider}


@app.post("/v1/character-sheets")
def create_character_sheet(request: CharacterSheetRequest):
    """Validate and route an authorized 4K character-sheet request to ComfyUI."""
    try:
        spec = CharacterSheetSpec(
            subject_name=request.subject_name,
            reference_labels=tuple(request.reference_labels),
            consent_granted=request.consent_granted,
        )
        payload = build_character_sheet_payload(spec)
        job = CreativeJob(
            intent="character-sheet",
            capabilities=("image-to-image", "face-consistency"),
            payload=payload,
            local_only=True,
            consent_granted=True,
        )
        provider = CapabilityRouter(Registry()).route(job)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    except Exception as exc:
        raise HTTPException(422, str(exc)) from exc
    return {
        "job_id": "character-sheet-" + str(abs(hash(request.subject_name))),
        "status": "queued",
        "provider": provider,
        "output": {"width": spec.width, "height": spec.height, "format": "png", "panels": spec.panels},
        "payload": payload,
    }
