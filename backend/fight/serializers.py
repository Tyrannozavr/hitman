from rest_framework import serializers
from .models import Fight

class FightSerializers(serializers.ModelSerializer):
    # user = serializers.CharField(max_length=255)
    attack = serializers.CharField(max_length=255)
    defend = serializers.CharField(max_length=255)
    class Meta:
        model = Fight
        fields = ['user', 'attack', 'defend']

    def create(self, validated_data):
        print('serializer')
        # print(validated_data)
        # print('1')
        user = validated_data.get('user')
        attack = validated_data.get('attack')
        defend = validated_data.get('defend')
        # attack = [1, 2, 3]
        # defend = [1, 2, 3]
        # print(user, attack, defend, type(user), type(attack), type(defend))
        print(user, attack)
        user = 1
        return Fight.objects.create(user_id=user, attack=attack, defend=defend)
