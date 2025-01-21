import uvicorn
from dvpn.api.routes import app
from config.settings import SERVER_HOST, SERVER_PORT, DEBUG

if __name__ == "__main__":
    uvicorn.run(
        "dvpn.api.routes:app",
        host=SERVER_HOST,
        port=SERVER_PORT,
        reload=DEBUG
    )