from abc import ABC, abstractmethod

class ResponseStrategy(ABC):
    @abstractmethod
    def generate_response(self):
        pass

class ActiveUserResponseStrategy(ResponseStrategy):
    def generate_response(self):
        return "ActiveUserResponseStrategy"

class IdleUserResponseStrategy(ResponseStrategy):
    def generate_response(self):
        return "IdleUserResponseStrategy"

class NewUserResponseStrategy(ResponseStrategy):
    def generate_response(self):
        return "NewUserResponseStrategy"