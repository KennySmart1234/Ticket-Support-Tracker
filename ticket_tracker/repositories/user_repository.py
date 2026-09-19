from sqlalchemy.orm import Session
from models.user import User
from models.user_role import UserRole


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user


    def get_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_username(self, username: str) -> User | None:
        return self.db.query(User).filter(User.username == username).first()

    def get_all(self) -> list[User]:
        return self.db.query(User).all()

    def get_support_agents(self) -> list[User]:
        return (self.db.query(User).filter(User.role == UserRole.SUPPORT_AGENT).order_by(User.agent_number).all())

    def get_customers(self) -> list[User]:
        return self.db.query(User).filter(User.role == UserRole.CUSTOMER).order_by(User.id).all()
