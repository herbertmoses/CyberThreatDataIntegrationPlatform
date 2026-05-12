from app.utils.hash_util import (
    generate_event_hash
)


def normalize_cloud(log):

    payload = log["payload"]

    source = "cloud"

    asset = payload.get("instance_id")

    event_type = payload.get("event_type")

    severity_map = {
        1: "low",
        5: "medium",
        9: "critical"
    }

    severity = severity_map.get(payload.get("severity_level"), "unknown")


    return {
        "source": source,
        "asset": asset,
        "event_type": event_type,
        "severity": severity,
        "event_hash":
            generate_event_hash(
                source,
                asset,
                event_type,
                severity
            ),
        "raw_data": payload
    }