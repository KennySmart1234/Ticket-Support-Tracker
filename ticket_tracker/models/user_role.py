from enum import Enum

class UserRole(str, Enum):
    CUSTOMER = "CUSTOMER"
    SUPPORT_AGENT = "SUPPORT_AGENT"
    ADMIN = "ADMIN"