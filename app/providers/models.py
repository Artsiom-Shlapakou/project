from django.db import models
from django_countries.fields import CountryField


class ProviderType(models.TextChoices):
    FACTORY = 0
    DISTRIBUTOR = 1
    Dealership = 2
    LARGE_REATAIL = 3
    INDIVIDUAL_ENTREPRENEUR = 4


class Address(models.Model):
    country = CountryField()
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f'\
        {self.country}, \
        {self.city}, \
        {self.street}, \
        {self.house_number}'

    class Meta():
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class Contacts(models.Model):
    email = models.EmailField()
    address = models.OneToOneField(to=Address, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.email

    class Meta():
        verbose_name = 'Contacts'
        verbose_name_plural = 'Contacts'


class Provider(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type_provider = models.CharField(
        choices=ProviderType.choices,
        max_length=10
    )
    contacts = models.OneToOneField(
        to=Contacts,
        on_delete=models.CASCADE
    )
    provider = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='providers'
    )
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name}, {self.type_provider}'
