import secrets
import string

def generate_ticket_number(length: int=8) -> str:
    """Generate cryptographically secure ticket number"""
    secure_ticket_number = "".join(secrets.choice(string.digits) for _ in range(length))
    return secure_ticket_number
