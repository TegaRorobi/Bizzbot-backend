from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins
from rest_framework.decorators import action
from .serializers import *

from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

from django.contrib.auth import get_user_model
UserModel = get_user_model()


class LoginView(TokenObtainPairView):
    @swagger_auto_schema(
        operation_summary='Get a user\'s JWT refresh and access tokens.',
        operation_description='Takes a set of user credentials (email and password) and returns '
        'an access and refresh JSON web\ntoken pair to prove the authentication of those credentials.'
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class LoginRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        operation_summary='Refresh a user\'s JWT access token with a refresh token.',
        operation_description='Takes a user\'s refresh token and generates a new access token from it and returns it.'
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class LogoutView(TokenBlacklistView):
    @swagger_auto_schema(
        operation_summary='Invalidate a user\'s JWT refresh token',
        operation_description='Takes a user\'s refresh token and blacklists it, thereby invalidating it as a form of logout.'
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


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
    
    @swagger_auto_schema(
        operation_summary='Delete a specific user',
        operation_description='This endpoint accepts the id of a user as a path parameter, '
        'searches for the user in the database and deletes the user completely.'
    )
    def destroy(self, *args, **kwargs):
        return super().destroy(*args, **kwargs)


class ProductsViewSet(viewsets.ModelViewSet):
    
    "API Viewset to create, retrieve, list out and retrieve products."

    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Product.objects.prefetch_related('seller').filter(seller=self.request.user).order_by('-id')
    
    @swagger_auto_schema(
        operation_summary='List out all products offered by the currently authenticated user.',
        operation_description='Accepts the page number as a query parameter and returns a '
        'paginated response of all the products offered by the currently authenticated user.'
    )
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Create a new product',
        operation_description='Accepts the common parameters of a product, but doesn\'t accept the seller id. '
        'The seller id is automatically gotten from the currently authenticated user.'
    )
    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

    @swagger_auto_schema(
        operation_summary='Retrieve a specific product by id',
        operation_description='Accepts the id of the product as a path parameter, searches for the product '
        'in the database, and returns details of the specific product.'
    )
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='Update all writeable fields of a specific product',
        operation_description='This endpoint accepts the id of the product as a path parameter, '
        'searches for the product in the database, and attempts to update ALL fields of the product.\n'
        'Note: The PATCH method to this endpoint might be a safer option, depending on the use case.'
    )
    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='Update some details of a specific product',
        operation_description='This endpoint accepts the id of a product as a path parameter, '
        'searches for the product in the database, and updates only the fields sent in the request body.\n'
        'Note: This is a safer and less rigid alternative to the PUT method of the same endpoint.'
    )
    def partial_update(self, *args, **kwargs):
        return super().partial_update(*args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='Delete a specific product',
        operation_description='This endpoint accepts the id of a product as a path parameter, '
        'searches for the product in the database and deletes the product completely.'
    )
    def destroy(self, *args, **kwargs):
        return super().destroy(*args, **kwargs)


class OpeningDaysViewSet(viewsets.ModelViewSet):
    
    "API Viewset to list out, create, retrieve, update and delete the opening days of a user."

    serializer_class = OpeningDaySerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return self.request.user.opening_days.order_by('-id')


