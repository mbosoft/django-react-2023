from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from core.user.serializers import UserSerializers
from core.user.models import User
from rest_framework.permissions import AllowAny


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ('patch','get')
    #permission_classes =(IsAuthenticated)
    #permission_classes =(AllowAny)
    serializer_class = UserSerializers

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)


    def get_object(self):
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request,obj)
        return obj