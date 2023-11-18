
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import *

from django_countries.serializers import CountryFieldMixin
from django.contrib.auth import get_user_model
UserModel = get_user_model()

class UserSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, validated_data):
        clear_password = validated_data['password']
        validated_data['password'] = make_password(clear_password)
        validated_data.setdefault('is_active', 'True')
        return super().create(validated_data)


class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    class Meta:
        model = Product
        fields = '__all__'