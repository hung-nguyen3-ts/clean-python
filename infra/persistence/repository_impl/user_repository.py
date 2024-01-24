from domain.repositories.user_repository import UserRepository
from domain.entities.user import User
from infra.persistence.orm.user_orm_model import UserORMModel, Base
from sqlalchemy.orm import Session


class SqlUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_id(self, user_id):
        user_record = self.session.query(UserORMModel).filter(UserORMModel.id == user_id).first()
        if user_record:
            return User(state=user_record.state)
        return None
