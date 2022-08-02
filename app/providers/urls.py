from django.urls import path, include
from rest_framework.routers import DefaultRouter

from providers.views import ProviderViewSet, send_mail_api

app_name = "providers"

router = DefaultRouter()
router.register(r'providers', ProviderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('providers/<int:id>/send_qr_code', send_mail_api,  name='send_qr_code'),
]
