from django.urls import path
from .views import FightView

app_name = 'fight'
urlpatterns = [
    path('', FightView.as_view(), name='fight'),
]