from rest_framework import serializers
from .models import Fight

class FightSerializers(serializers.ModelSerializer):
    user = serializers.IntegerField(max_value=255)
    attack = serializers.ListField(default=[])
    defend = serializers.ListField(default=[])

    class Meta:
        model = Fight
        fields = ['user', 'attack', 'defend']

    def create(self, validated_data):
        user = validated_data.get('user')
        attack = validated_data.get('attack')
        defend = validated_data.get('defend')
        return Fight.objects.create(user_id=user, attack=attack, defend=defend)

