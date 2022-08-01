from rest_framework import serializers

from products.models import Product
from providers.serializers import ProviderSerializer


class ProductSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer()
    
    class Meta:
        model = Product
        fields = (
            'name',
            'model',
            'release_date',
            'provider'
        )
