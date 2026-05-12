from fastapi import FastAPI
from app.routes import automate

app = FastAPI(
    title="CTIP - Automation Service"
)

app.include_router(
    automate.router,
    prefix="/automate"
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