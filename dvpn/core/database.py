# dvpn/core/database.py
import sqlite3
from contextlib import contextmanager
from typing import Generator
from .models import Node, NetworkBlock
import logging

class DatabaseService:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.setup_database()
    
    @contextmanager
    def get_connection(self) -> Generator[sqlite3.Connection, None, None]:
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        finally:
            conn.close()
    
    def setup_database(self):
        with self.get_connection() as conn:
            c = conn.cursor()
            
            # Create nodes table
            c.execute('''
                CREATE TABLE IF NOT EXISTS nodes (
                    id TEXT PRIMARY KEY,
                    ip TEXT NOT NULL,
                    port INTEGER NOT NULL,
                    node_type TEXT NOT NULL,
                    public_key TEXT NOT NULL,
                    bandwidth REAL NOT NULL,
                    location TEXT NOT NULL,
                    stake REAL DEFAULT 0.0,
                    connected_clients INTEGER DEFAULT 0,
                    last_active REAL NOT NULL
                )
            ''')
            
            # Create blocks table
            c.execute('''
                CREATE TABLE IF NOT EXISTS blocks (
                    id TEXT PRIMARY KEY,
                    timestamp REAL NOT NULL,
                    sender_id TEXT NOT NULL,
                    receiver_id TEXT NOT NULL,
                    data_size INTEGER NOT NULL,
                    node_type TEXT NOT NULL,
                    FOREIGN KEY (sender_id) REFERENCES nodes (id),
                    FOREIGN KEY (receiver_id) REFERENCES nodes (id)
                )
            ''')
            
            # Create indexes
            c.execute('CREATE INDEX IF NOT EXISTS idx_nodes_type ON nodes(node_type)')
            c.execute('CREATE INDEX IF NOT EXISTS idx_blocks_timestamp ON blocks(timestamp)')
            
            conn.commit()

    async def save_node(self, node: Node):
        try:
            with self.get_connection() as conn:
                c = conn.cursor()
                c.execute('''
                    INSERT OR REPLACE INTO nodes 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    node.id, node.ip, node.port, node.node_type.value,
                    node.public_key, node.bandwidth, node.location,
                    node.stake, node.connected_clients, node.last_active
                ))
                conn.commit()
        except Exception as e:
            logging.error(f"Error saving node: {e}")
            raise

    async def save_block(self, block: NetworkBlock):
        try:
            with self.get_connection() as conn:
                c = conn.cursor()
                c.execute('''
                    INSERT INTO blocks 
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    block.id, block.timestamp, block.sender_id,
                    block.receiver_id, block.data_size, block.node_type.value
                ))
                conn.commit()
        except Exception as e:
            logging.error(f"Error saving block: {e}")
            raise