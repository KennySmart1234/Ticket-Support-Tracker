from models.user import User
from models.user_role import UserRole
from repositories.user_repository import UserRepository
from schemas.user import UserCreate


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create(self, data: UserCreate) -> User:

        existing_user = self.repository.get_by_username(data.username)

        if existing_user:
            raise ValueError("User already exists")

        user = User(
            fullname=data.fullname,
            username=data.username,
            password=data.password,
            role=UserRole.CUSTOMER
        )

        return self.repository.create(user)

    def get_by_id(self, user_id: int) -> User | None:
        return self.repository.get_by_id(user_id)

    def get_by_username(self, username: str) -> User | None:
        return self.repository.get_by_username(username)

    def get_all(self) -> list[User]:
        return self.repository.get_all()