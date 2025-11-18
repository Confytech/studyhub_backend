from rest_framework import serializers
from .models import Transaction, PremiumUnlock

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class PremiumUnlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumUnlock
        fields = '__all__'

