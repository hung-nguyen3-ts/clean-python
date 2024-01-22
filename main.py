import uvicorn
from infra.interfaces.fastapi_routes import app

from infra.interfaces.web.server import create_server

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    app = create_server()