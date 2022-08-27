from django.urls import path

from .views import Authenticate, LoginAPIView, RegistrationAPIView

app_name = 'authentication'
urlpatterns = [
    path('', Authenticate.as_view(), name='authenticate'),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
]