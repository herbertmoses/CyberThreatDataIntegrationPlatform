from app.utils.hash_util import (
    generate_event_hash
)


def normalize_edr(log):

    payload = log["payload"]

    source = "edr"

    asset = payload.get("host")

    event_type = payload.get("threat")

    severity = payload.get("severity")

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