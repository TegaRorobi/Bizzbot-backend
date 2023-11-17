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
        operation_description='This endpoint returns a paginated response of '
        'all users stored in the database, with all necessary fields.'
    )
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Create a new user',
        operation_description='This endpoint accepts common parameters of a user, '
        'saves the user to the database and returns the created user.'
    )
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='Retrieve a specific user by id',
        operation_description='This endpoint accepts the id of a user as a path parameter, '
        'searches for the user in the database and returns the user.'
    )
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='Update all the details of a particular user',
        operation_description='This endpoint accepts the id of a user as a path parameter, '
        'searches for the user in the database, and attempts to update ALL fields of the user.\n'
        'Note: The PATCH method to this endpoint might be a safer option, depending on the use case.'
    )
    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='Update some details of a particular user',
        operation_description='This endpoint accepts the id of a user as a path parameter, '
        'searches for the user in the database, and updates only the fields sent in the request body.\n'
        'Note: This is a safer and less rigid alternative to the PUT method of the same endpoint.'
    )
    def partial_update(self, *args, **kwargs):
        return super().partial_update(*args, **kwargs)
    
    def destroy(self, *args, **kwargs):
        return super().destroy(*args, **kwargs)
