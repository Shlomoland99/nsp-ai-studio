from fastapi.testclient import TestClient
from backend.app.main import app
client=TestClient(app)
def test_health(): assert client.get("/health").json()["status"]=="ok"
def test_job_route():
    r=client.post("/v1/jobs",json={"intent":"poster","capabilities":["text-to-image"],"local_only":True})
    assert r.status_code==200 and r.json()["provider"]=="comfyui"