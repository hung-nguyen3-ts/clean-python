import uvicorn

from infra.interfaces.web.server import create_server

if __name__ == "__main__":
    app = create_server()
    uvicorn.run(app, host="0.0.0.0", port=8000)