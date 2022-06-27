from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=6,
        max_length=128,
        write_only=True
    )
    token = serializers.CharField(
        max_length=255,
        read_only=True
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)
        if username is None:
            raise serializers.ValidationError(
                'username is required for log in'
            )
        if password is None:
            raise serializers.ValidationError(
                'password is required for log in '
            )
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'user does not exist'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token,
        }
