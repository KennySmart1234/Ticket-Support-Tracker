from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from core.database import Base
from models.ticket_status import TicketStatus


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)

    ticket_number = Column(Integer, nullable=False, index=True)

    agent_ticket_number = Column(Integer, nullable=False)

    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)

    status = Column(
        String,
        default=TicketStatus.OPEN.value,
        nullable=False
    )

    customer_id = Column(
        Integer,
        ForeignKey("user.id"),
        nullable=False
    )

    assigned_agent_id = Column(
        Integer,
        ForeignKey("user.id"),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    closed_at = Column(DateTime, nullable=True)

    customer = relationship(
        "User",
        foreign_keys=[customer_id],
        back_populates="tickets"
    )

    assigned_agent = relationship(
        "User",
        foreign_keys=[assigned_agent_id],
        back_populates="assigned_tickets"
    )