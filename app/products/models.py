from django.db import models

from providers.models import Provider
from products.validations import validate_release_date


class Product(models.Model):
    name = models.CharField(max_length=25)
    model = models.CharField(max_length=50)
    release_date = models.DateField(validators=[validate_release_date])    

    providers = models.ManyToManyField(to=Provider, related_name='products')
    
    def __str__(self) -> str:
        return f'{self.name}, {self.model}, {self.pk}'
