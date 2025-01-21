import time
from typing import Optional
from ..core.models import NetworkBlock, NodeType

class BlockManager:
    def __init__(self):
        self.current_block: Optional[NetworkBlock] = None
    
    def create_block(self, sender_id: str, receiver_id: str, 
                    data_size: int, node_type: NodeType) -> NetworkBlock:
        """Create a new network block"""
        block = NetworkBlock(
            id=f"block_{int(time.time())}_{sender_id}_{receiver_id}",
            timestamp=time.time(),
            sender_id=sender_id,
            receiver_id=receiver_id,
            data_size=data_size,
            node_type=node_type
        )
        self.current_block = block
        return block
    
    def get_current_block(self) -> Optional[NetworkBlock]:
        """Get the current block"""
        return self.current_block