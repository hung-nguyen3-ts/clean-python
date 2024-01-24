from domain.entities.conversation import Conversation
from domain.exceptions.entity_not_found_exception import EntityNotFoundException
from domain.repositories.message_repository import MessageRepository
from domain.repositories.user_repository import UserRepository


class MessageService:
    def __init__(self, message_repository: MessageRepository, user_repository: UserRepository):
        self.message_repository = message_repository
        self.user_repository = user_repository

    def handle_message(self, user_id, message_content):
        user = self.user_repository.get_user_by_id(user_id)

        if not user:
            raise EntityNotFoundException("User", user_id)

        message = self.message_repository.create_message(user_id, message_content)

        conversation = Conversation(user, message)

        response_message = conversation.response()

        self.message_repository.save_message(response_message)

        return response_message
