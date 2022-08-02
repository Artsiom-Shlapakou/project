from django.http import HttpResponse
from django_filters import rest_framework as filters
from django.db.models import Avg, DecimalField
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, api_view
from rest_framework_api_key.permissions import HasAPIKey

from employees.permissions import IsActiveUser
from providers.models import Provider
from providers.serializers import ProviderSerializer
from providers.filters import ProviderFilterSet
from providers.tasks import send_qr_code_to_email


class ProviderViewSet(ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProviderFilterSet

    @action(detail=False, methods=['GET'])
    def objects_with_debt(self, request):
        avg_debt = self.queryset.aggregate(
            avg_debt=Avg('debt', output_field=DecimalField(max_digits=10, decimal_places=2)))
        self.queryset = self.queryset.filter(debt__gte=avg_debt['avg_debt'])
        return self.list(request)

    def get_permissions(self):
        permission_classes = [IsActiveUser]
        if self.action == 'update':
            permission_classes.append(HasAPIKey)

        return [permission() for permission in permission_classes]


@api_view()
def send_mail_api(request, id):
    send_qr_code_to_email.delay(id)

    return HttpResponse('Sent QR code to email')
