from rest_framework import serializers
from .models import Fight, Statistic, User

class FightSerializers(serializers.ModelSerializer):
    attack = serializers.ListField(default=[])
    defend = serializers.ListField(default=[])

    class Meta:
        model = Fight
        fields = '__all__'

    def create(self, validated_data):
        print('create')
        user = validated_data.get('user')
        attack = validated_data.get('attack')
        defend = validated_data.get('defend')
        print(2, validated_data)
        print(user, attack, defend)
        return Fight.objects.create(user=user, attack=attack, defend=defend)

class StatisticSerializer(serializers.ModelSerializer):
    queryset = Statistic.objects.all()
    first_player = FightSerializers(many=False, read_only=True)
    second_player = FightSerializers(many=False, read_only=True)

    class Meta:
        model = Statistic
        fields = '__all__'
