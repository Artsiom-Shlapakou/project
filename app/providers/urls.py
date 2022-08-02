from django.urls import path, include
from rest_framework.routers import DefaultRouter

from providers.views import ProviderViewSet, send_mail_api

app_name = "providers"

router = DefaultRouter()
router.register(r'', ProviderViewSet)


urlpatterns = [
    path('providers/', include(router.urls)),
    path('providers/<int:id>/qr', send_mail_api,  name='qr-code-contacts'),
]
