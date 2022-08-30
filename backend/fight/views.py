import json

from authentication.models import User
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Fight, Statistic
from .permissions import FightPermission
from .serializers import FightSerializers, StatisticSerializer


def score(user_one, user_two):
    """Counted scores after fight"""
    one_attack = user_one.attack
    one_defend = user_one.defend
    two_attack = user_two.attack
    two_defend = user_two.defend
    scores = {'голова': 3, 'туловище': 2, 'левая рука': 1, 'правая рука': 1, 'левая нога': 1, 'правая нога': 1}
    one_score = [scores[i] if i not in two_defend else 0 for i in one_attack]
    two_score = [scores[i] if i not in one_defend else 0 for i in two_attack]
    return sum(one_score), sum(two_score)

def fight():
    players = Fight.objects.filter(finished=False)[:2]
    if len(players) < 2:
        return False
    one_score, two_score = score(players[0], players[1])
    for i in players:
        i.finished = True
        i.save()
    num = Statistic.objects.last().num_round + 1 if len(Statistic.objects.all()) > 0 else 1
    return Statistic.objects.create(num_round=num, first_player=players[0], second_player=players[1],
                                    first_player_score=one_score, second_player_score=two_score)

class StatisticView(APIView):
    serializer_class = StatisticSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Statistic.objects.all()

    def get(self, request):
        """preparing data before send"""
        data = Statistic.objects.all()
        data = [i.__dict__ for i in data]

        for i in data: #replacing user link with user data and user_id with user.username
            i.pop('_state')
            i['first_player'] = Fight.objects.get(id=i.pop('first_player_id')).__dict__
            i['first_player'].pop('_state')
            i['second_player'] = Fight.objects.get(id=i.pop('second_player_id')).__dict__
            i['second_player'].pop('_state')
            i['first_player']['user'] = User.objects.get(id=i['first_player'].pop('user_id')).username
            i['second_player']['user'] = User.objects.get(id=i['second_player'].pop('user_id')).username

            redundant_data = ['id', 'finished']   #removing redundant data
            for j in redundant_data:
                i['first_player'].pop(j)
                i['second_player'].pop(j)
        return Response(data)


class FightView(APIView):
    serializer_class = FightSerializers
    permission_classes = (FightPermission,)

    def post(self, request):
        data = request.data
        data['user'] = request.user.username
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        obj = fight()
        if not obj:
            return Response(data={
                "detail": 'fight only one user'
            }, status=status.HTTP_201_CREATED)
        return Response(data={
            'num_round': obj.num_round,
            'first_player_id': obj.first_player_id,
            'second_player_id': obj.second_player_id,
            'first_player_score': obj.first_player_score,
            'second_player_score': obj.second_player_score
        }, status=status.HTTP_201_CREATED)




