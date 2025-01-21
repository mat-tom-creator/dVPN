import json
import time
from typing import Any, Dict
from dataclasses import asdict

def serialize_to_json(obj: Any) -> str:
    """Serialize object to JSON string"""
    if hasattr(obj, '__dict__'):
        return json.dumps(asdict(obj))
    return json.dumps(obj)

def generate_id(prefix: str) -> str:
    """Generate unique ID with prefix"""
    return f"{prefix}_{int(time.time())}_{hash(time.time())}"

def calculate_bandwidth(data_size: int, time_elapsed: float) -> float:
    """Calculate bandwidth in MB/s"""
    return (data_size / 1024 / 1024) / time_elapsed