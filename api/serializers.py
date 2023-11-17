
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

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