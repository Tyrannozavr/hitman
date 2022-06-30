from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer, LoginSerializer
from .renderers import UserJsonRenderers


class RegistrationAPIView(APIView):
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)
    renderer_classes = (UserJsonRenderers,)

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    renderer_classes = (UserJsonRenderers,)

    def post(self, request):
        # print(request.data)
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)

class LoginAPIView2(APIView):
    serializer_class = LoginSerializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJsonRenderers,)

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)

