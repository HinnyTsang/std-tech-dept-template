"""Pre generate hook"""
import re

def validate_author_email(email: str):
    """Validate email"""
    email_pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
    assert re.match(email_pattern, email), "Invalid email"

validate_author_email("{{ cookiecutter.author_email }}")
