from fastapi import WebSocket, WebSocketDisconnect
from typing import Dict
import json
import logging
from ..network.manager import NetworkManager

class WebSocketManager:
    def __init__(self, network_manager: NetworkManager):
        self.network_manager = network_manager
        self.active_connections: Dict[str, WebSocket] = {}
    
    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        self.active_connections[client_id] = websocket
    
    async def disconnect(self, client_id: str):
        if client_id in self.active_connections:
            del self.active_connections[client_id]
    
    async def broadcast(self, message: dict):
        for connection in self.active_connections.values():
            try:
                await connection.send_json(message)
            except Exception as e:
                logging.error(f"Error broadcasting message: {e}")