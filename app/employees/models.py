from django.db import models
from providers.models import Provider
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'


class Employee(AbstractBaseUser):
    email = models.EmailField(unique=True)
    
    username = models.CharField(
        db_index=True,
        max_length=50,
        unique=True,
    )

    birthday = models.DateField(blank=True)

    gender = models.CharField(
        max_length=1,
        choices=Gender.choices
    )
    is_active = models.BooleanField(default=True)
    last_visit = models.DateTimeField(auto_now_add=True)
    
    provider = models.ForeignKey(
        to=Provider,
        on_delete=models.CASCADE
    )
    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["username", "birthday",]

    def __str__(self):
        return self.username
