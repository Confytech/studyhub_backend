from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'coins', 'is_premium']
        read_only_fields = ['coins', 'is_premium']

