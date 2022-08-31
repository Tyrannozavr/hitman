import django.http
from rest_framework import permissions
from django.core.exceptions import PermissionDenied
from django.http.response import HttpResponse

from .models import Fight


class FightPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        """this function checks that the user cannot fight himself and is authenticated"""
        # if not request.user.is_authenticated:
        #     print('no authenticated')
        #     return HttpResponse('unautorized', status=401)

        if len(Fight.objects.all()) > 0 and request.user == Fight.objects.last().user \
                and not Fight.objects.last().finished or not request.user.is_authenticated:
            return False
        return True
