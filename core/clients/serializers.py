from django_countries.serializer_fields import CountryField

from rest_framework import serializers

from models.client.models import Client


class ClientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        style={
            'placeholder': 'Name',
            'autofocus': True
        }
    )

    email = serializers.EmailField(
        style={
            'placeholder': 'Email',
            'autofocus': True,
            'input_type': 'email'
        },
        required=True
    )

    phone_number = serializers.CharField(
        style={
            'placeholder': 'Phone number',
            'autofocus': True
        }
    )

    contact_name = serializers.CharField(
        style={
            'placeholder': 'Contact name',
            'autofocus': True
        }
    )
    street_name = serializers.CharField(
        style={
            'placeholder': 'Street name',
            'autofocus': True
        }
    )

    suburb = serializers.CharField(
        style={
            'placeholder': 'Suburb',
            'autofocus': True
        }
    )

    post_code = serializers.CharField(
        style={
            'placeholder': 'Postal code',
            'autofocus': True
        }
    )

    state = CountryField(
        style={
            'placeholder': 'State',
            'autofocus': True
        }
    )

    class Meta:
        model = Client
        fields = '__all__'
