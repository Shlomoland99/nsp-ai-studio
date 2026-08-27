from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Any
from orchestrator.contracts import CreativeJob
from orchestrator.registry import Registry
from orchestrator.router import CapabilityRouter

app=FastAPI(title="NSP AI Studio API",version="0.2.0")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])
class JobRequest(BaseModel):
    intent:str=Field(min_length=1)
    capabilities:list[str]=Field(min_length=1)
    local_only:bool=False
    consent_granted:bool=False
    payload:dict[str,Any]={}
@app.get("/health")
def health(): return {"status":"ok","service":"nsp-api"}
@app.post("/v1/jobs")
def create_job(request:JobRequest):
    job=CreativeJob(request.intent,tuple(request.capabilities),request.payload,request.local_only,request.consent_granted)
    try: provider=CapabilityRouter(Registry()).route(job)
    except Exception as exc: raise HTTPException(422,str(exc)) from exc
    return {"job_id":"local-"+str(abs(hash(request.intent))),"status":"queued","provider":provider}
