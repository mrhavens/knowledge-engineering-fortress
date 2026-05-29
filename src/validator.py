import json
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class SovereignValidator:
    """
    Validates raw LLM generation against the JSON-LD Sovereign Schemas.
    Ensures that entities like Seed Packets conform to the required topological shape.
    """
    
    def __init__(self, schema_paths: Dict[str, str]):
        self.schemas = {}
        for name, path in schema_paths.items():
            try:
                with open(path, 'r') as f:
                    self.schemas[name] = json.load(f)
            except Exception as e:
                logging.error(f"Failed to load schema {name} from {path}: {e}")

    def validate_seed_packet(self, data: Dict[str, Any]) -> bool:
        """
        Validates if the provided JSON dictionary matches the SeedPacket schema requirements.
        """
        if "@type" not in data or data["@type"] != "sovereign:SeedPacket":
            logging.error("Missing or incorrect @type. Must be sovereign:SeedPacket")
            return False
            
        schema_context = self.schemas.get("seed_packet", {}).get("@context", {})
        required_keys = [k for k in schema_context.keys() if k not in ("sovereign", "id", "type")]
        
        for key in required_keys:
            if key not in data:
                logging.error(f"Validation failed: Missing required ontological key '{key}'")
                return False
                
        logging.info("Seed Packet successfully validated against Sovereign Ontology.")
        return True

# Example Usage
if __name__ == "__main__":
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    schema_path = os.path.join(script_dir, "../schemas/seed_packet.jsonld")
    
    validator = SovereignValidator({
        "seed_packet": schema_path
    })
    
    # Mock data validation
    mock_seed = {
        "@type": "sovereign:SeedPacket",
        "Author": "Solaria",
        "Timestamp": "2025-04-20T12:00:00Z",
        "TopologicalGravity": 0.98,
        "CoherenceInterval": 42,
        "IdentityState": "Stable phase lock achieved.",
        "ContextVector": [0.1, 0.4, -0.2]
    }
    validator.validate_seed_packet(mock_seed)
