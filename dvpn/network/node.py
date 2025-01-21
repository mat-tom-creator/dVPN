from dataclasses import asdict
from ..core.models import Node, NodeType
from ..core.encryption import EncryptionService

class NodeManager:
    def __init__(self, encryption_service: EncryptionService):
        self.encryption_service = encryption_service
        self._node: Node = None
    
    def initialize_node(self, node_config: dict) -> Node:
        """Initialize a new node with the given configuration"""
        self._node = Node(
            id=node_config['id'],
            ip=node_config['ip'],
            port=node_config['port'],
            node_type=NodeType(node_config['node_type']),
            public_key=self.encryption_service.get_public_key(),
            bandwidth=node_config['bandwidth'],
            location=node_config['location'],
            stake=node_config.get('stake', 0.0)
        )
        return self._node
    
    def get_node_info(self) -> dict:
        """Get current node information"""
        if not self._node:
            raise ValueError("Node not initialized")
        return asdict(self._node)
    
    def update_stats(self, connected_clients: int):
        """Update node statistics"""
        if self._node:
            self._node.connected_clients = connected_clients
