import datetime
from django.core.exceptions import ValidationError


def validate_birthday(birthday):
    if birthday > datetime.date.today():
        raise ValidationError("The birthday can't be in future")
