from fastapi import FastAPI
from app.routes import ingest

app = FastAPI(title="CTIP - Ingestion Service")

app.include_router(ingest.router, prefix="/ingest")

# -----------------------------------
# Health Check
# -----------------------------------

@app.get("/")
def health():

    return {
        "status":
            "normalization-service running"
    }