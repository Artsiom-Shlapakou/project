import datetime
from django.core.exceptions import ValidationError


def validate_release_date(release_date):
    if release_date > datetime.date.today():
        raise ValidationError("The release date can't be in future")
