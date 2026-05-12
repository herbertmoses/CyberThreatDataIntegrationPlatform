THREAT_DB = {

    "ransomware": {
        "cve": "CVE-2025-1234",
        "risk_score": 95,
        "threat_category": "malware",
        "recommended_action":
            "Isolate endpoint immediately"
    },

    "unauthorized_access": {
        "cve": "CVE-2025-8888",
        "risk_score": 80,
        "threat_category": "intrusion",
        "recommended_action":
            "Rotate credentials and audit IAM roles"
    }
}


def enrich_threat(event_type):

    return THREAT_DB.get(
        event_type,
        {
            "cve": "unknown",
            "risk_score": 20,
            "threat_category": "unknown",
            "recommended_action":
                "Manual investigation required"
        }
    )