from django.core.exceptions import ValidationError
import re

def validate_password(password, user=None):
    if len(password) < 12:
        raise ValidationError("Password must be at least 12 characters long.")

    if not re.search(r'[a-z]', password):
        raise ValidationError("Password must contain at least one lowercase letter.")

    if not re.search(r'[A-Z]', password):
        raise ValidationError("Password must contain at least one uppercase letter.")

    if not re.search(r'\d', password):
        raise ValidationError("Password must contain at least one number.")

    if not re.search(r'[!@#$%^&*()_+=\-[\]{};:\'",.<>?]', password):
        raise ValidationError("Password must contain at least one symbol (!@#$%^&*()_+=-[]{};:'\",.<>?).")

    if user and (user.username.lower() in password.lower() or user.email.lower() in password.lower()):
        raise ValidationError("Password cannot contain the username or email.")

