from sqlalchemy import Column, Integer, String, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import relationship

from core.database import Base
from models.user_role import UserRole


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    role = Column(SQLEnum(UserRole), nullable=False)
    tickets = relationship("Ticket", foreign_keys= "Ticket.customer_id", back_populates="customer")
    assigned_tickets = relationship("Ticket", foreign_keys="Ticket.assigned_agent_id", back_populates="assigned_agent")
    assigned_agent_id = Column(Integer, ForeignKey("user.id"), nullable=True)