from application.command.chat_command import ChatCommand
from application.response.chat_response import ChatResponse
from domain.services.message_service import MessageService

class MessageService:
    def __init__(self, message_service: MessageService):
        self.message_service = message_service

    def handle_message(self, chat_command: ChatCommand) -> ChatResponse:
        response = self.message_service.handle_message(
            user_id=chat_command.user_id,
            message_content=chat_command.content
        )
        return ChatResponse(message=response.message)