from rest_framework import serializers
from .models import Fight, Statistic

class FightSerializers(serializers.ModelSerializer):
    # user = serializers.IntegerField(max_value=255)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    attack = serializers.ListField(default=[])
    defend = serializers.ListField(default=[])

    class Meta:
        model = Fight
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data.get('user')
        attack = validated_data.get('attack')
        defend = validated_data.get('defend')
        return Fight.objects.create(user_id=user, attack=attack, defend=defend)

class StatisticSerializer(serializers.ModelSerializer):
    queryset = Statistic.objects.all()
    first_player = FightSerializers(many=False, read_only=True)
    second_player = FightSerializers(many=False, read_only=True)

    class Meta:
        model = Statistic
        fields = '__all__'
        # fields = ['num_round', 'first_player_attack']
