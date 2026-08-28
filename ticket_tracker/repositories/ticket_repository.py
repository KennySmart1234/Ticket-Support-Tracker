
from sqlalchemy.orm import Session
from models.ticket import Ticket

class TicketRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, ticket: Ticket) -> Ticket:

        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)

        return ticket

    def get_by_id(self, ticket_id: int) -> Ticket | None:
        return self.db.query(Ticket).filter(Ticket.id == ticket_id).first()

    def get_all(self) -> list[Ticket]:
        return self.db.query(Ticket).all()

    def get_by_customer(self, customer_id: int) -> list[Ticket]:
        return self.db.query(Ticket).filter(Ticket.customer_id == customer_id).all()


    def get_customer_agent(self, customer_id: int) -> int | None:
        ticket = (self.db.query(Ticket)
                  .filter(Ticket.customer_id == customer_id)
                  .filter(Ticket.assigned_agent_id.isnot(None))
                  .first())

        if ticket:
            return ticket.assigned_agent_id

        return None

    def get_agent_ticket_count(self, agent_id: int) -> int:
        return self.db.query(Ticket).filter(Ticket.assigned_agent_id == agent_id).count()



    def update(self, ticket:Ticket) -> Ticket:
        self.db.commit()
        self.db.refresh(ticket)

        return ticket

