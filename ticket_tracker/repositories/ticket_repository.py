from sqlalchemy.orm import Session

from models.ticket import Ticket


class TicketRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        ticket: Ticket,
        agent_id: int,
        ticket_number: int,
        agent_ticket_number: int
    ) -> Ticket:

        ticket.assigned_agent_id = agent_id
        ticket.ticket_number = ticket_number
        ticket.agent_ticket_number = agent_ticket_number

        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)

        return ticket

    def get_next_ticket_number(self) -> int:
        last_ticket = (
            self.db.query(Ticket)
            .order_by(Ticket.ticket_number.desc())
            .first()
        )

        if last_ticket:
            return last_ticket.ticket_number + 1

        return 1

    def get_agent_ticket_count(self, agent_id: int) -> int:
        return (
            self.db.query(Ticket)
            .filter(Ticket.assigned_agent_id == agent_id)
            .count()
        )

    def get_by_id(self, ticket_id: int) -> Ticket | None:
        return (
            self.db.query(Ticket)
            .filter(Ticket.id == ticket_id)
            .first()
        )

    def get_all(self) -> list[Ticket]:
        return self.db.query(Ticket).all()

    def get_by_customer(self, customer_id: int) -> list[Ticket]:
        return (
            self.db.query(Ticket)
            .filter(Ticket.customer_id == customer_id)
            .all()
        )

    def update(self, ticket: Ticket) -> Ticket:
        self.db.commit()
        self.db.refresh(ticket)

        return ticket