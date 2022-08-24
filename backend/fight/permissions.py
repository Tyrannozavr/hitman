from rest_framework import permissions

class FightPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        print('permissions')
        # print(self, request.__dict__, view)
        return False, 'hello'
