from pydantic import BaseModel

from application.command.chat_command import ChatCommand


class ChatRequest(BaseModel):
    content: str
    user_id: str

    def to_command(self):
        return ChatCommand(
            content=self.content,
            user_id=self.user_id
        )