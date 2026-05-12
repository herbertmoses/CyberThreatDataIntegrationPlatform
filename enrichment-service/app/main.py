from fastapi import FastAPI
from app.routes import enrich

app = FastAPI(
    title="CTIP - Enrichment Service"
)

app.include_router(
    enrich.router,
    prefix="/enrich"
)

# -----------------------------------
# Health Check
# -----------------------------------

@app.get("/")
def health():

    return {
        "status":
            "normalization-service running"
    }