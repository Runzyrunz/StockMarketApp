from rest_framework import serializers
from .models import Account  # Assuming 'Account' is a model

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
