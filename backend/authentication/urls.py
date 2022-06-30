from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, LoginAPIView2


app_name = 'authentication'
urlpatterns = [
    # path('', index, name='index'),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('test/', LoginAPIView2.as_view()),
]