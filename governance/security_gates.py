def evaluate_ethics_and_fraud_safety(payload: dict) -> bool:
        forbidden = ["unauthorized_access", "data_exfiltration"]
        vectors = payload.get("vectors", [])
        return not any(v in forbidden for v in vectors)
    
    def classify_risk(payload: dict) -> str:
        if payload.get("network_egress") and payload.get("root_privilege"):
            return "CRITICAL"
        return "LOW"
    
