from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
import json

from .models import Fight
from .serializers import FightSerializers

class FightView(APIView):
    serializer_class = FightSerializers
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        data['user'] = request.user.pk
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # serializer.is_valid(raise_exception=True)
        return Response(data=json.dumps({
            'created': 'true'
        }), status=status.HTTP_200_OK)
