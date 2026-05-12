# from fastapi import FastAPI
# from app.routes import normalize
#
# app = FastAPI(
#     title="CTIP - Normalization Service"
# )
#
# app.include_router(
#     normalize.router,
#     prefix="/normalize"
# )

from fastapi import FastAPI

import threading

from app.kafka_consumer import (
    consume_events
)

from app.routes import normalize

app = FastAPI(
    title="CTIP - Normalization Service"
)


# -----------------------------------
# Start Kafka Consumer
# -----------------------------------

@app.on_event("startup")
def startup_event():

    thread = threading.Thread(
        target=consume_events,
        daemon=True
    )

    thread.start()


# -----------------------------------
# Routes
# -----------------------------------

app.include_router(
    normalize.router,
    prefix="/normalize"
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