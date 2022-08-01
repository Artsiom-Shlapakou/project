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
    # list_filter = ('city',)
    
    def provider_link(self, obj):
        if provider := obj.provider:
            link=reverse("admin:providers_provider_change", args=[obj.provider])
            return mark_safe(f'<a href="{link}">{provider}</a>')
    
    provider_link.allow_tags=True
    provider_link.short_description = 'Provider_link'

    @admin.action(description='Liquidation of debt to the provider')
    def liquidate_supplier_debt(self, request, queryset):
        queryset.update(debt=0)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'address')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'house_number')
    list_filter = ('city',)
