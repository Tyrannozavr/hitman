from django.urls import path
from .views import technice_view


urlpatterns = [
    path('', technice_view)
]