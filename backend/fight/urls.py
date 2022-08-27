from django.urls import path

from .views import FightView, StatisticView

app_name = 'fight'
urlpatterns = [
    path('', FightView.as_view(), name='fight'),
    path('statistic/', StatisticView.as_view(), name='statistic'),
    # path('statistic/', StatisticView2.as_view({'get': 'list'}), name='statistic'),
]