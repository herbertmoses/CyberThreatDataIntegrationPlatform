from fastapi import APIRouter
from app.database import (
    raw_collection,
    normalized_collection
)

from app.normalizers.edr import normalize_edr
from app.normalizers.cloud import normalize_cloud
from app.normalizers.cicd import normalize_cicd

router = APIRouter()


@router.post("/")
def normalize_logs():

    # logs = list(raw_collection.find())

    logs = list(
        raw_collection.find(
            {"normalized": False}
        )
    )

    normalized_count = 0

    for log in logs:

        source = log.get("source")

        if source == "edr":
            normalized = normalize_edr(log)

        elif source == "cloud":
            normalized = normalize_cloud(log)

        elif source == "cicd":
            normalized = normalize_cicd(log)

        else:
            continue

        existing = normalized_collection.find_one(
            {
                "event_hash":
                    normalized["event_hash"]
            }
        )

        if existing:
            continue

        normalized_collection.insert_one(normalized)

        raw_collection.update_one(
            {"_id": log["_id"]},
            {
                "$set": {
                    "normalized": True
                }
            }
        )

        normalized_count += 1

    return {
        "status": "success",
        "normalized_logs": normalized_count
    }


# ----------------------------------------
# GET RAW LOGS
# ----------------------------------------

@router.get("/raw")
def get_raw_logs():

    logs = list(raw_collection.find({}, {"_id": 0}))

    return {
        "count": len(logs),
        "data": logs
    }


# ----------------------------------------
# GET NORMALIZED LOGS
# ----------------------------------------

@router.get("/normalized")
def get_normalized_logs():

    logs = list(
        normalized_collection.find({}, {"_id": 0})
    )

    return {
        "count": len(logs),
        "data": logs
    }


# ----------------------------------------
# FILTER BY SEVERITY
# ----------------------------------------

@router.get("/normalized/severity/{severity}")
def get_by_severity(severity: str):

    logs = list(
        normalized_collection.find(
            {"severity": severity},
            {"_id": 0}
        )
    )

    return {
        "severity": severity,
        "count": len(logs),
        "data": logs
    }