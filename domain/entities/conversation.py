from typing import Any

from domain.entities.message import Message
from domain.entities.user import User
from pydantic import BaseModel


class Conversation(BaseModel):
    user: User
    message: Message

    def __init__(self, user, message, **data: Any):
        super().__init__(**data)
        self.user = user
        self.message = message
        self.response_strategy = user.get_strategy_for_state()

    def response(self):
        return self.response_strategy.generate_response()
