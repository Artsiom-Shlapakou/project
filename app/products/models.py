from django.db import models

from providers.models import Provider
from products.validations import validate_release_date


class Product(models.Model):
    name = models.CharField(max_length=25)
    model = models.CharField(max_length=50)
    release_date = models.DateField(validators=[validate_release_date])    
    
    provider = models.ForeignKey(
        to=Provider,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.name}, {self.model}'


class ProviderProduct(models.Model):
    provider_id = models.ForeignKey(to=Provider, on_delete=models.CASCADE)
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE)
