from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import *

from drf_yasg.utils import swagger_auto_schema

from django.contrib.auth import get_user_model
UserModel = get_user_model()


class UsersViewSet(viewsets.ModelViewSet):

    "API Viewset to list out, create, retrieve, update and delete users."

    queryset = UserModel.objects.order_by('-id')
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_summary='List out all users',
        operation_description='This endpoint returns a paginated response of all users stored in the database, with all necessary fields.'
    )
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)
    
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)
    
    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)
    
    def partial_update(self, *args, **kwargs):
        return super().partial_update(*args, **kwargs)
    
    def destroy(self, *args, **kwargs):
        return super().destroy(*args, **kwargs)
