import hashlib


def generate_event_hash(
    source,
    asset,
    event_type,
    severity
):

    raw_string = (
        f"{source}-"
        f"{asset}-"
        f"{event_type}-"
        f"{severity}"
    )

    return hashlib.sha256(
        raw_string.encode()
    ).hexdigest()