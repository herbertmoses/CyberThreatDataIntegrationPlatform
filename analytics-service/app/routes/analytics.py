from fastapi import APIRouter

from pymongo import MongoClient

from sqlalchemy.orm import Session

from sqlalchemy import func

from app.database import (
    SessionLocal,
    engine
)

from app.models import (
    Base,
    SecurityEvent
)

Base.metadata.create_all(bind=engine)

router = APIRouter()

mongo_client = MongoClient(
    "mongodb://mongodb:27017"
)

mongo_db = mongo_client["ctip"]

enriched_collection = (
    mongo_db["enriched_logs"]
)


@router.post("/sync")
def sync_events():

    db: Session = SessionLocal()

    logs = list(
        enriched_collection.find(
            {},
            {"_id": 0}
        )
    )

    inserted = 0

    for log in logs:

        existing = db.query(
            SecurityEvent
        ).filter(
            SecurityEvent.asset
            == log.get("asset"),

            SecurityEvent.event_type
            == log.get("event_type")
        ).first()

        if existing:
            continue

        event = SecurityEvent(

            source=log.get("source"),

            asset=log.get("asset"),

            event_type=log.get("event_type"),

            severity=log.get("severity"),

            risk_score=log.get("risk_score"),

            threat_category=
                log.get("threat_category"),

            recommended_action=
                log.get(
                    "recommended_action"
                )
        )

        db.add(event)

        inserted += 1

    db.commit()

    db.close()

    return {
        "status": "success",
        "inserted": inserted
    }

@router.get("/top-risk-assets")
def top_risk_assets():

    db: Session = SessionLocal()

    results = db.query(
        SecurityEvent.asset,
        SecurityEvent.risk_score
    ).order_by(
        SecurityEvent.risk_score.desc()
    ).limit(10).all()

    db.close()

    return {
        "data": [
            {
                "asset": r[0],
                "risk_score": r[1]
            }
            for r in results
        ]
    }


@router.get("/severity-distribution")
def severity_distribution():

    db: Session = SessionLocal()

    results = db.query(
        SecurityEvent.severity,
        func.count()
    ).group_by(
        SecurityEvent.severity
    ).all()

    db.close()

    return {
        "data": [
            {
                "severity": r[0],
                "count": r[1]
            }
            for r in results
        ]
    }