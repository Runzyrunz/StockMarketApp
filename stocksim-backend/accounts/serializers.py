from rest_framework import serializers
from .models import Account, Portfolio  # Import Portfolio model

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'  # Adjust fields as necessary for your portfolio data structure
