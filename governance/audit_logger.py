import hashlib
    import json
    import time
    
    class ImmutableAuditLogger:
        def __init__(self):
            self.ledger = []
    
        def log_event(self, chain_id: str, data: dict):
            entry = {"id": chain_id, "data": data, "ts": time.time()}
            entry_hash = hashlib.sha256(json.dumps(entry).encode()).hexdigest()
            self.ledger.append({"hash": entry_hash, "entry": entry})
    
