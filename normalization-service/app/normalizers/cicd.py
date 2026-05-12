from app.utils.hash_util import (
    generate_event_hash
)


def normalize_cicd(log):

    payload = log["payload"]

    source = "cicd"

    asset = payload.get("repository")

    event_type = payload.get("issue")

    severity = payload.get("priority")




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