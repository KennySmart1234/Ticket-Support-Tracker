from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

from dependencies import get_db
from models.user import User
from repositories.user_repository import UserRepository
from schemas.user import UserCreate, UserResponse
from services.user_service import UserService

router = APIRouter(prefix="/user", tags=["users"])

@router.post("/", response_model=UserResponse)
def create_user(data: UserCreate, db: Session = Depends(get_db)):

    repository = UserRepository(db)
    service = UserService(repository)

    try:
        return service.create(data)

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    repository = UserRepository(db)
    service = UserService(repository)

    return service.get_all()