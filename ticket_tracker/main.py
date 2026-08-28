from fastapi import FastAPI

from core.database import Base, engine
from models.user import User
from models.ticket import Ticket

from routers.ticket_router import router as ticket_router
from routers.user_router import router as user_router

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(ticket_router)
app.include_router(user_router)
