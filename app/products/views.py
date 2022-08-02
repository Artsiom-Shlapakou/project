from rest_framework.viewsets import ModelViewSet
from rest_framework_api_key.permissions import HasAPIKey

from products.models import Product
from products.serializers import ProductSerializer
from employees.permissions import IsActiveUser


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        permission_classes = [IsActiveUser]
        if self.action == 'update':
            permission_classes.append(HasAPIKey)

        return [permission() for permission in permission_classes]
