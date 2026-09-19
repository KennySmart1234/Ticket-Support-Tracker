from core.database import SessionLocal
from models.user import User
from models.ticket import Ticket
from models.user_role import UserRole
from repositories.user_repository import UserRepository


def seed_agents():

    db = SessionLocal()

    repository = UserRepository(db)

    agents = [
        {
            "fullname": "Agent One",
            "username": "agent1",
            "password": "password1",
            "agent_number": 1
        },
        {
            "fullname": "Agent Two",
            "username": "agent2",
            "password": "password2",
            "agent_number": 2
        },
        {
            "fullname": "Agent Three",
            "username": "agent3",
            "password": "password3",
            "agent_number": 3
        },
        {
            "fullname": "Agent Four",
            "username": "agent4",
            "password": "password4",
            "agent_number": 4
        },
        {
            "fullname": "Agent Five",
            "username": "agent5",
            "password": "password5",
            "agent_number": 5
        }
    ]

    for agent_data in agents:

        existing_agent = repository.get_by_username(
            agent_data["username"]
        )

        if existing_agent:

            # Make sure existing agents have
            # the correct agent number.
            existing_agent.agent_number = agent_data["agent_number"]

            db.commit()

            continue

        agent = User(
            fullname=agent_data["fullname"],
            username=agent_data["username"],
            password=agent_data["password"],
            role=UserRole.SUPPORT_AGENT,
            agent_number=agent_data["agent_number"]
        )

        repository.create(agent)

    db.close()


seed_agents()