from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Fight
from .serializers import FightSerializers

class FightView(APIView):
    serializer_class = FightSerializers
    permission_classes = (AllowAny,)

    def post(self, request):
        print('view')
        # print(request.data, request.user, request.headers)
        data = request.data
        data['user'] = request.user.pk
        # data['attack'] = [1, 2, 3]
        # data['defend'] = [1, 2, 3]
        # data['attack'] = '[1,2,3]'
        # data['defend'] = '[1,2,3]'
        print('attack', data.get('attack'), type(data.get('attack')))
        # print(data)
        # print(request.data)
        print('data', data)
        serializer = self.serializer_class(data=data)

        # print(serializer.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        print('end')
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
