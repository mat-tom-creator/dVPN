from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from ..core.models import Node, NetworkBlock
from ..network.manager import NetworkManager

router = APIRouter()
network_manager = NetworkManager()

@router.get("/", response_class=HTMLResponse)
async def get_dashboard():
    with open("static/index.html") as f:
        return f.read()

@router.post("/nodes")
async def register_node(node: Node):
    await network_manager.register_node(node)
    return {"status": "success", "node_id": node.id}