
from fastapi import FastAPI, HTTPException, status
from application.services.message_service import MessageService

from infra.interfaces.dto.chat_request_dto import ChatRequest

app = FastAPI()

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    try:
        message_service = MessageService() # TODO: inject this dependency
        response = message_service.handle_message(chat_request.to_command())
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
