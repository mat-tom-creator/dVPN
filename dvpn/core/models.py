# dvpn/core/models.py
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Optional
from datetime import datetime

class NodeType(Enum):
    PROVIDER = "provider"
    CLIENT = "client"

@dataclass
class Node:
    id: str
    ip: str
    port: int
    node_type: NodeType
    public_key: str
    bandwidth: float
    location: str
    stake: float = 0.0
    connected_clients: int = 0
    last_active: float = 0.0

@dataclass
class NetworkBlock:
    id: str
    timestamp: float
    sender_id: str
    receiver_id: str
    data_size: int
    node_type: NodeType

@dataclass
class NetworkStats:
    total_nodes: int
    active_providers: int
    connected_clients: int
    total_bandwidth: float
    total_blocks: int