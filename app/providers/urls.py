from django.urls import path
from providers.views import ProviderListAPIView

app_name = "providers"


urlpatterns = [
    path('providers/', ProviderListAPIView.as_view()),
]
