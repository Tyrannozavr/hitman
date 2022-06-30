from rest_framework import serializers
from .models import Fight

class FightSerializers(serializers.ModelSerializer):
    # user = serializers.CharField(max_length=255)
    attack = serializers.CharField(max_length=255)
    defend = serializers.CharField(max_length=255)
    class Meta:
        model = Fight
        fields = ['attack', 'defend']