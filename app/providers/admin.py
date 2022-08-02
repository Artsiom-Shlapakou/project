from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe    
from django.contrib import messages
from django.utils.translation import ngettext
from providers.models import (
    Provider,
    Contacts,
    Address,
)


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_provider', 'contacts', 'debt', 'provider_link')
    actions = ['liquidate_supplier_debt']
    readonly_fields = ('provider_link',)
    list_filter = ('contacts__address__city',)
    
    def provider_link(self, obj):
        if provider := obj.provider:
            link=reverse("admin:providers_provider_change", args=[obj.provider.id])
            return mark_safe(f'<a href="{link}">{provider}</a>')
    
    provider_link.allow_tags=True
    provider_link.short_description = 'Provider_link'

    @admin.action(description='Liquidation of debt to the provider')
    def liquidate_supplier_debt(self, request, queryset):
        updated = queryset.update(debt=0)
        self.message_user(request, ngettext(
            '%d debt was successfully reduced to zero.',
            '%d debts were successfully reduced to zero.',
            updated,
        ) % updated, messages.SUCCESS)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'address')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'house_number')
    list_filter = ('city',)
