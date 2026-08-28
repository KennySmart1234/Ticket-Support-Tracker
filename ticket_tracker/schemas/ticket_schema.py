from datetime import datetime
from pydantic import BaseModel
from models.ticket_status import TicketStatus

class TicketCreate(BaseModel):
    title: str
    description: str
    customer_id:int

class TicketResponse(BaseModel):
    id:int
    ticket_number:int
    title: str
    description: str
    status: TicketStatus
    customer_id: int
    assigned_agent_id: int | None
    created_at: datetime
    updated_at: datetime
    closed_at: datetime | None

    model_config = {
        "from_attributes": True
    }


class TicketStatusUpdate(BaseModel):
    status: TicketStatus