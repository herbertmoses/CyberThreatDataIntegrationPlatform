from fastapi import APIRouter

from app.database import (
    normalized_collection,
    enriched_collection
)

from app.enrichers.threat_mapper import enrich_threat

router = APIRouter()


@router.post("/")
def enrich_logs():

    # logs = list(normalized_collection.find())

    logs = list(
        normalized_collection.find(
            {
                "enriched": {
                    "$ne": True
                }
            }
        )
    )

    enriched_count = 0

    for log in logs:

        enrichment = enrich_threat(
            log.get("event_type")
        )

        enriched_log = {

            "source": log.get("source"),
            "asset": log.get("asset"),
            "event_type": log.get("event_type"),
            "severity": log.get("severity"),

            "cve": enrichment["cve"],
            "risk_score": enrichment["risk_score"],
            "threat_category":
                enrichment["threat_category"],
            "recommended_action":
                enrichment["recommended_action"],

            "raw_data": log.get("raw_data")
        }

        enriched_collection.insert_one(enriched_log)

        normalized_collection.update_one(
            {"_id": log["_id"]},
            {
                "$set": {
                    "enriched": True
                }
            }
        )

        enriched_count += 1

    return {
        "status": "success",
        "enriched_logs": enriched_count
    }


@router.get("/")
def get_enriched_logs():

    logs = list(
        enriched_collection.find({}, {"_id": 0})
    )

    return {
        "count": len(logs),
        "data": logs
    }