# config/settings.py
import os

DATABASE_PATH = os.getenv("DVPN_DB_PATH", "dvpn_network.db")
SERVER_HOST = os.getenv("DVPN_HOST", "0.0.0.0")
SERVER_PORT = int(os.getenv("DVPN_PORT", "8000"))
DEBUG = os.getenv("DVPN_DEBUG", "False").lower() == "true"