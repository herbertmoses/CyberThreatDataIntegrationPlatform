def evaluate_rules(log):

    alerts = []

    risk_score = log.get("risk_score", 0)

    severity = log.get("severity")

    event_type = log.get("event_type")

    # -----------------------------------
    # Critical Risk Rule
    # -----------------------------------

    if risk_score >= 90:

        alerts.append({
            "alert_type": "critical_risk",
            "message":
                f"Critical threat detected: {event_type}",
            "action":
                "Immediate SOC escalation required"
        })

    # -----------------------------------
    # Ransomware Rule
    # -----------------------------------

    if event_type == "ransomware":

        alerts.append({
            "alert_type": "ransomware_detected",
            "message":
                "Potential ransomware attack",
            "action":
                "Isolate endpoint immediately"
        })

    # -----------------------------------
    # Critical Severity Rule
    # -----------------------------------

    if severity == "critical":

        alerts.append({
            "alert_type": "critical_severity",
            "message":
                "Critical severity event identified",
            "action":
                "Open incident response workflow"
        })

    return alerts