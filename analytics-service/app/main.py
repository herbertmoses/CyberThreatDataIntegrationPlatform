from fastapi import FastAPI

from app.routes import analytics

app = FastAPI(
    title="CTIP - Analytics Service"
)

app.include_router(
    analytics.router,
    prefix="/analytics"
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