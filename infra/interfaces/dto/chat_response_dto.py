from pydantic import BaseModel

class ChatRequest(BaseModel):
    content: str

    def from_dto(c):
        return ChatCommand(
            content=self.content,
            user_id=self.user_id
        )