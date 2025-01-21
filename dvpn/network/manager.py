from typing import Dict
from fastapi import WebSocket
import json
import time
from ..core.models import Node, NetworkBlock, NetworkStats
from ..core.database import DatabaseService

class NetworkManager:
    def __init__(self, db_service: DatabaseService):
        self.db_service = db_service
        self.active_nodes: Dict[str, Node] = {}
        self.connected_clients: Dict[str, WebSocket] = {}
    
    async def register_node(self, node: Node):
        node.last_active = time.time()
        self.active_nodes[node.id] = node
        await self.db_service.save_node(node)
        await self.broadcast_network_update()
    
    async def create_block(self, sender_id: str, receiver_id: str, data_size: int):
        block = NetworkBlock(
            id=f"block_{int(time.time())}_{sender_id}_{receiver_id}",
            timestamp=time.time(),
            sender_id=sender_id,
            receiver_id=receiver_id,
            data_size=data_size,
            node_type=self.active_nodes[sender_id].node_type
        )
        await self.db_service.save_block(block)
        await self.broadcast_block(block)