from rest_framework import serializers

from providers.models import Provider
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    providers = serializers.PrimaryKeyRelatedField(many=True, queryset=Provider.objects.all())
    
    class Meta:
        model = Product
        fields = (
            'name',
            'model',
            'release_date',
            'providers'
        )
