from rest_framework import serializers
from core.models import User, TrafficJam
from django.http import JsonResponse

# Serializer: Convert model to json format

# User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'is_active',
        ]

#Traffic Jam
class TrafficJamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficJam
        fields = ['id', 'date', 'time', 'message']
