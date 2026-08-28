from fastapi import Depends

from core.database import SessionLocal
from repositories.ticket_repository import TicketRepository

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

def get_ticket_repository(db = Depends(get_db)):
    return TicketRepository(db)