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
    one_attack = user_one.attack
    one_defend = user_one.defend
    two_attack = user_two.attack
    two_defend = user_two.defend
    scores = {'0': 3, '1': 2, '2': 1, '3': 1, '4': 1, '5': 1}
    one_score = [scores[i] if i not in two_defend else 0 for i in one_attack]
    two_score = [scores[i] if i not in one_defend else 0 for i in two_attack]
    return sum(one_score), sum(two_score)

class StatisticView(viewsets.ModelViewSet):
    serializer_class = StatisticSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Statistic.objects.all()

    def post(self, request):
        players = Fight.objects.filter(finished=False)[:2]
        if len(players) < 2:
            return 'please wait'
        one_score, two_score = score(players[0], players[1])
        for i in players:
            i.finished = True
            i.save()
        num = Statistic.objects.last().num_round + 1 if len(Statistic.objects.all()) > 0 else 1 # set num round
        return Statistic.objects.create(num_round=num, first_player=players[0], second_player=players[1],
                                        first_player_score=one_score, second_player_score=two_score)

class FightView(APIView):
    serializer_class = FightSerializers
    permission_classes = (IsAuthenticated,)


    def post(self, request):

        if len(Fight.objects.all()) > 0 and request.user == Fight.objects.last().user and not Fight.objects.last().finished:
            return Response(data='please wait', status=status.HTTP_306_RESERVED)
        data = request.data
        data['user'] = request.user.username
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # print('created', StatisticView.post(1, 2))   #it is required for created statistic, not simple print
        obj = StatisticView.post(1, 2)
        print(obj.__dict__)
        print('hello', obj.num_round)
        # в случае отрицательного доступа obj это строка
        return Response(data=json.dumps({
            'num_round': obj.num_round
        }), status=status.HTTP_201_CREATED)




