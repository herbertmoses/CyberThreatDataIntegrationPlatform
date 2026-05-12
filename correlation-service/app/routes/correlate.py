from fastapi import APIRouter

from app.database import (
    enriched_collection,
    correlation_collection
)

from app.engines.correlator import (
    correlate_events
)

router = APIRouter()


@router.post("/")
def run_correlation():

    logs = list(
        enriched_collection.find(
            {},
            {"_id": 0}
        )
    )

    findings = correlate_events(logs)

    inserted = 0

    for finding in findings:

        correlation_collection.insert_one(
            finding
        )

        inserted += 1

    return {
        "status": "success",
        "correlations_created":
            inserted
    }


@router.get("/")
def get_correlations():

    findings = list(
        correlation_collection.find(
            {},
            {"_id": 0}
        )
    )

    return {
        "count": len(findings),
        "data": findings
    }