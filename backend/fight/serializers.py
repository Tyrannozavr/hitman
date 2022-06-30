from rest_framework import serializers
from .models import Fight

class FightSerializers(serializers.Serializer):
    user = serializers.CharField(max_length=255)
    # attack = serializers.CharField(max_length=255)
    # defend = serializers.CharField(max_length=255)
    attack = serializers.ListField(default=[])
    defend = serializers.ListField(default=[])
    # class Meta:
    #     model = Fight
    #     fields = ['user', 'attack', 'defend']

    def create(self, validated_data):
        print('serializer')
        # print(validated_data)
        # print('1')
        user = validated_data.get('user')
        attack = validated_data.get('attack')
        defend = validated_data.get('defend')
        # print('111', attack, type(attack))
        # attack = [1, 2, 3]
        # defend = [1, 2, 3]
        # print(user, attack, defend, type(user), type(attack), type(defend))
        print(user, attack)
        user = 1
        return Fight.objects.create(user_id=user, attack=attack, defend=defend)

    def validate(self, data):
        print('validate', data)
        return data
