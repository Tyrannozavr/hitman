from rest_framework import serializers
from .models import Fight, Statistic, User

class FightSerializers(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    # snippets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # user = serializers.RelatedField(many=True, read_only=True)
    # user = serializers.ReadOnlyField(source='user.username')
    # user = serializers.RelatedField(source='user.username', queryset=User.objects.all())
    attack = serializers.ListField(default=[])
    defend = serializers.ListField(default=[])

    class Meta:
        model = Fight
        fields = '__all__'

    def create(self, validated_data):
        # print('create', validated_data)
        user = User.objects.get(username=validated_data.get('user').get('username'))
        attack = validated_data.get('attack')
        defend = validated_data.get('defend')
        # print(2, validated_data)
        # print('data', user, attack, defend)
        return Fight.objects.create(user=user, attack=attack, defend=defend)

class StatisticSerializer(serializers.ModelSerializer):
    queryset = Statistic.objects.all()
    first_player = FightSerializers(many=False, read_only=True)
    second_player = FightSerializers(many=False, read_only=True)

    class Meta:
        model = Statistic
        fields = '__all__'
