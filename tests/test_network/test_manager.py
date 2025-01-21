import pytest
from dvpn.network.manager import NetworkManager
from dvpn.core.database import DatabaseService
from dvpn.core.models import Node, NodeType

@pytest.fixture
def network_manager():
    db_service = DatabaseService(":memory:")
    return NetworkManager(db_service)

async def test_register_node(network_manager):
    node = Node(
        id="test_node",
        ip="127.0.0.1",
        port=8000,
        node_type=NodeType.PROVIDER,
        public_key="test_key",
        bandwidth=100.0,
        location="US"
    )
    await network_manager.register_node(node)
    assert node.id in network_manager.active_nodes