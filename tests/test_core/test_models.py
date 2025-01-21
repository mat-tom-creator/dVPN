import pytest
from dvpn.core.models import Node, NetworkBlock, NodeType

def test_node_creation():
    node = Node(
        id="test_node",
        ip="127.0.0.1",
        port=8000,
        node_type=NodeType.PROVIDER,
        public_key="test_key",
        bandwidth=100.0,
        location="US"
    )
    assert node.id == "test_node"
    assert node.node_type == NodeType.PROVIDER
    assert node.connected_clients == 0

def test_network_block_creation():
    block = NetworkBlock(
        id="test_block",
        timestamp=123456789.0,
        sender_id="sender",
        receiver_id="receiver",
        data_size=1000,
        node_type=NodeType.PROVIDER
    )
    assert block.id == "test_block"
    assert block.data_size == 1000