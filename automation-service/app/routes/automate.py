from fastapi import APIRouter

from app.database import (
    enriched_collection,
    alerts_collection
)

from app.rules.rule_engine import (
    evaluate_rules
)

router = APIRouter()


@router.post("/")
def run_automation():

    # logs = list(enriched_collection.find())

    logs = list(
        enriched_collection.find(
            {
                "automated": {
                    "$ne": True
                }
            }
        )
    )

    generated_alerts = 0

    for log in logs:

        alerts = evaluate_rules(log)

        for alert in alerts:

            alert_document = {

                "asset": log.get("asset"),

                "event_type":
                    log.get("event_type"),

                "severity":
                    log.get("severity"),

                "risk_score":
                    log.get("risk_score"),

                "alert_type":
                    alert["alert_type"],

                "message":
                    alert["message"],

                "recommended_action":
                    alert["action"]
            }

            alerts_collection.insert_one(
                alert_document
            )

            enriched_collection.update_one(
                {"_id": log["_id"]},
                {
                    "$set": {
                        "automated": True
                    }
                }
            )

            generated_alerts += 1

    return {
        "status": "success",
        "alerts_generated":
            generated_alerts
    }


@router.get("/")
def get_alerts():

    alerts = list(
        alerts_collection.find({}, {"_id": 0})
    )

    return {
        "count": len(alerts),
        "data": alerts
    }