from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework import viewsets

from .models import Fight, Statistic
from .serializers import FightSerializers, StatisticSerializer

class StatisticView(viewsets.ModelViewSet):
    serializer_class = StatisticSerializer
    permission_classes = (AllowAny,)
    queryset = Statistic.objects.all()
    # def get(self, request):
    #     print('statistic')
    #     data = list(Statistic.objects.all())
    #     print(data)
    #     serializer = self.serializer_class(data=data, many=True)
    #     serializer.is_valid(raise_exception=True)
    #     return Response(data=serializer.data)

    def post(self, request):
        players = Fight.objects.filter(finished=False)[:2]
        if len(players) < 2:
            return 'please wait'
        for i in players:
            i.finished = True
            i.save()
        num = Statistic.objects.last().num_round + 1 if len(Statistic.objects.all() )> 0 else 1
        return Statistic.objects.create(num_round=num, first_player=players[0], second_player=players[1])


class FightView(APIView):
    serializer_class = FightSerializers
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        if len(Fight.objects.all()) > 0 and request.user == Fight.objects.last().user:
            # print('post', request.user, Fight.objects.last().user)
            # print('please wait')
            # print(StatisticView.post(1, 2))
            return Response(data=json.dumps({
                'message': 'please wait'
            }), status=status.HTTP_306_RESERVED)

        data = request.data
        data['user'] = request.user.pk
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # print('created')
        return Response(data=json.dumps({
            'created': 'true'
        }), status=status.HTTP_306_RESERVED)




