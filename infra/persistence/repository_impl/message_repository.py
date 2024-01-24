from domain.repositories.message_repository import MessageRepository
from domain.entities.message import Message
from infra.persistence.orm.message_orm_model import MessageORMModel, Base
from sqlalchemy.orm import Session


class SqlMessageRepository(MessageRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_message(self, content):
        return Message(content=content)

    def save_message(self, message):
        message_record = MessageORMModel(content=message.content)
        self.session.add(message_record)
        self.session.commit()
