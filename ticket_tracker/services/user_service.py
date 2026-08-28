from models.user import User
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository


    def create(self, user: User) -> User:
        existing_user = self.repository.get_by_username(user.username)

        if existing_user:
            raise ValueError("User already exists")

        return self.repository.create(user)

    def get_by_id(self, user_id: int) -> User | None:
        return self.repository.get_by_id(user_id)

    def get_by_username(self, username: str) -> User | None:
        return self.repository.get_by_username(username)

    def get_all(self) -> list[User]:
        return self.repository.get_all()