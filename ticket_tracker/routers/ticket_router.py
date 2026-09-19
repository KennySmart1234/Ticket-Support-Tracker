from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from dependencies import get_db
from models.ticket import Ticket
from repositories.ticket_repository import TicketRepository
from repositories.user_repository import UserRepository
from schemas.ticket_schema import TicketStatusUpdate, TicketCreate, TicketResponse
from services.ticket_service import TicketService

router = APIRouter(prefix="/tickets", tags=["tickets"])

@router.post("/", response_model=TicketResponse)
def create_ticket(data: TicketCreate, db: Session = Depends(get_db)):
    repository = TicketRepository(db)
    user_repository = UserRepository(db)
    service = TicketService(repository, user_repository)

    ticket = Ticket(
        title=data.title,
        description=data.description,
        customer_id=data.customer_id
    )

    try:
        return service.create(ticket)

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )

@router.get("/")
def get_tickets(db: Session = Depends(get_db)):
    repository = TicketRepository(db)
    user_repository = UserRepository(db)

    service = TicketService(repository, user_repository)

    return service.get_all()


@router.get("/customer/{customer_id}", response_model=list[TicketResponse])
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    repository = TicketRepository(db)
    user_repository = UserRepository(db)

    service = TicketService(repository, user_repository)

    return service.get_by_customer(customer_id)


@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    repository = TicketRepository(db)
    user_repository = UserRepository(db)

    service = TicketService(repository, user_repository)

    ticket = service.get_by_id(ticket_id)

    if ticket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket not found"
        )

    return ticket


@router.patch("/{ticket_id}/status")
def update_ticket_status(
    ticket_id: int,
    data: TicketStatusUpdate,
    db: Session = Depends(get_db)
):
    repository = TicketRepository(db)
    user_repository = UserRepository(db)

    service = TicketService(repository, user_repository)

    try:
        return service.update_status(ticket_id, data.status)

    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket not found"
        )
