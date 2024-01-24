from abc import ABC, abstractmethod


class MessageRepository(ABC):
    @abstractmethod
    def create_message(self, user_id, content):
        pass

    @abstractmethod
    def save_message(self, message):
        pass
