from fastapi import FastAPI

def create_server() -> FastAPI:
    server = FastAPI()
    return server