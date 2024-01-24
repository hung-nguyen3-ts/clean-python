from enum import StrEnum
from typing import Any

from pydantic import BaseModel
from domain.strategies.response_strategy import (
    ActiveUserResponseStrategy,
    IdleUserResponseStrategy,
    NewUserResponseStrategy,
)


class UserState(StrEnum):
    INIT = "init"
    NEW_USER = "new_user"
    RETURNING_USER = "returning_user"
    IDLE_USER = "idle_user"
    ACTIVE_USER = "active_user"

class User(BaseModel):
    id: str
    state: UserState

    def __init__(self, id, state, **data: Any):
        super().__init__(**data)
        self.id = id
        self.state = state

    def get_strategy_for_state(self):
        if self.state == 'active':
            return ActiveUserResponseStrategy()
        elif self.state == 'idle':
            return IdleUserResponseStrategy()
        elif self.state == 'new':
            return NewUserResponseStrategy()
        else:
            raise ValueError(f"Unknown user state: {self.state}")