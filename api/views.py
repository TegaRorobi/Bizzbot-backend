from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import *

from django.contrib.auth import get_user_model
UserModel = get_user_model()


class UsersViewSet(viewsets.ModelViewSet):

    "API Viewset to list out, create, retrieve, update and delete users."

    queryset = UserModel.objects.order_by('-id')
    serializer_class = UserSerializer
