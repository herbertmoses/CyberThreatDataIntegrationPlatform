from collections import Counter


def correlate_events(logs):

    findings = []

    # -----------------------------------
    # Detect repeated event types
    # -----------------------------------

    event_counter = Counter(
        log["event_type"]
        for log in logs
    )

    for event_type, count in event_counter.items():

        if count >= 3:

            findings.append({

                "correlation_type":
                    "repeated_attack_pattern",

                "event_type":
                    event_type,

                "count":
                    count,

                "risk_level":
                    "high",

                "description":
                    f"Repeated {event_type} "
                    f"activity detected "
                    f"across multiple assets"
            })

    # -----------------------------------
    # Detect critical asset concentration
    # -----------------------------------

    # critical_assets = [
    #
    #     log["asset"]
    #
    #     for log in logs
    #
    #     if log.get("risk_score", 0) >= 90
    # ]

    critical_assets = list(set([

        log["asset"]

        for log in logs

        if log.get("risk_score", 0) >= 90
    ]))

    if len(critical_assets) >= 2:

        findings.append({

            "correlation_type":
                "critical_asset_cluster",

            "affected_assets":
                critical_assets,

            "risk_level":
                "critical",

            "description":
                "Multiple high-risk assets detected"
        })

    return findings