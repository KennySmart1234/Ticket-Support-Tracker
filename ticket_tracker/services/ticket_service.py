from models.ticket import Ticket
from models.ticket_status import TicketStatus
from repositories.ticket_repository import TicketRepository

class TicketService:
    def __init__(self, repository: TicketRepository):
        self.repository = repository

    def create(self, ticket: Ticket) -> Ticket:
        return self.repository.create(ticket)

    def get_by_id(self, ticket_id: int) -> Ticket | None:
        return self.repository.get_by_id(ticket_id)

    def get_all(self) -> list[Ticket]:
        return self.repository.get_all()

    def get_by_customer(self, customer_id: int) -> list[Ticket]:
        return self.repository.get_by_customer(customer_id)


    def update_status(self, ticket_id: int, status: TicketStatus) -> Ticket:

        ticket = self.repository.get_by_id(ticket_id)

        if ticket is None:
            raise ValueError("Ticket not found")
        ticket.status = status.value

        return self.repository.update(ticket)