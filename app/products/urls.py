from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import ProductViewSet


app_name = "products"

router = DefaultRouter()
router.register(r'', ProductViewSet)


urlpatterns = [
    path('products/', include(router.urls)),
]
