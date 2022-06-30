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
        print(request.data, request.user)
        a = request.data.get('defend')
        # print(a['0'])
        serializer = self.serializer_class(request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)