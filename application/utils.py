from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager


class UnitOfWork:
    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory

    @contextmanager
    def start(self) -> Session:
        session: Session = self.session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
