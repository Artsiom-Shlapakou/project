from providers.models import Address, Contacts, Provider
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'country',
            'city',
            'street',
            'house_number'
        )


class ContactsSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Contacts
        fields = (
            'email',
            'address'
        )
    

class ProviderSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer()

    class Meta:
        model = Provider
        fields = (
            'name',
            'type_provider',
            'contacts',
            'provider',
            'debt',
            'created'
        )
