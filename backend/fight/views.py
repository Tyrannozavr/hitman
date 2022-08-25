from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework import viewsets


from .permissions import FightPermission
from .models import Fight, Statistic
from .serializers import FightSerializers, StatisticSerializer


def score(user_one, user_two):
    """Counted scores after fight"""
    one_attack = user_one.attack
    one_defend = user_one.defend
    two_attack = user_two.attack
    two_defend = user_two.defend
    scores = {'0': 3, '1': 2, '2': 1, '3': 1, '4': 1, '5': 1}
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

class StatisticView(viewsets.ModelViewSet):
    serializer_class = StatisticSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Statistic.objects.all()


class FightView(APIView):
    serializer_class = FightSerializers
    permission_classes = (FightPermission,)

    def post(self, request):
        data = request.data
        data['user'] = request.user.username
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # obj = StatisticView.post(1, 2)
        obj = fight()
        if not obj:
            return Response(data=json.dumps({
                "detail": 'fight only one user'
            }), status=status.HTTP_201_CREATED)
        return Response(data=json.dumps({
            'num_round': obj.num_round,
            'first_player_id': obj.first_player_id,
            'second_player_id': obj.second_player_id,
            'first_player_score': obj.first_player_score,
            'second_player_score': obj.second_player_score
        }), status=status.HTTP_201_CREATED)




