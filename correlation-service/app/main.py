from fastapi import FastAPI
from app.routes import correlate

app = FastAPI(
    title="CTIP - Correlation Service"
)

app.include_router(
    correlate.router,
    prefix="/correlate"
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