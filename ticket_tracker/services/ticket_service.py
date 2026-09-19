from models.ticket import Ticket
from models.ticket_status import TicketStatus
from models.user_role import UserRole
from repositories.ticket_repository import TicketRepository
from repositories.user_repository import UserRepository


class TicketService:

    def __init__(
        self,
        repository: TicketRepository,
        user_repository: UserRepository
    ):
        self.repository = repository
        self.user_repository = user_repository

    def create(self, ticket: Ticket) -> Ticket:

        customer = self.user_repository.get_by_id(ticket.customer_id)

        if customer is None:
            raise ValueError("Customer not found")

        if customer.role != UserRole.CUSTOMER:
            raise ValueError("Only customers can create tickets")

        agents = self.user_repository.get_support_agents()

        if not agents:
            raise ValueError("No support agents available")

        ticket_number = self.repository.get_next_ticket_number()

        agent_index = (ticket_number - 1) % len(agents)

        agent = agents[agent_index]

        agent_ticket_number = (
                self.repository.get_agent_ticket_count(agent.id) + 1
        )

        return self.repository.create(
            ticket=ticket,
            agent_id=agent.id,
            ticket_number=ticket_number,
            agent_ticket_number=agent_ticket_number
        )


    def get_by_id(self, ticket_id: int) -> Ticket | None:
        return self.repository.get_by_id(ticket_id)

    def get_all(self) -> list[Ticket]:
        return self.repository.get_all()

    def get_by_customer(self, customer_id: int) -> list[Ticket]:
        return self.repository.get_by_customer(customer_id)

    def update_status(
        self,
        ticket_id: int,
        status: TicketStatus
    ) -> Ticket:

        ticket = self.repository.get_by_id(ticket_id)

        if ticket is None:
            raise ValueError("Ticket not found")

        ticket.status = status.value

        return self.repository.update(ticket)