
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import *
from .models2 import *

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django_countries.serializers import CountryFieldMixin
from django.contrib.auth import get_user_model
UserModel = get_user_model()

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        return {
            **super().validate(attrs), **{
                'id':self.user.id,
                'full_name': self.user.full_name,
                'email': self.user.email,
                'phone_number': self.user.phone_number,
                'country': self.user.country.name,
                'city': self.user.city
            }
        }

class UserSerializer(CountryFieldMixin, serializers.ModelSerializer):
    country_display = serializers.CharField(source='country.name', read_only=True)
    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, validated_data):
        clear_password = validated_data['password']
        validated_data['password'] = make_password(clear_password)
        validated_data.setdefault('is_active', 'True')
        return super().create(validated_data)


class ProductSerializer(serializers.ModelSerializer):
    seller_id = serializers.PrimaryKeyRelatedField(read_only=True, source='seller', many=False)
    seller_display = serializers.CharField(read_only=True, source='seller.__str__')
    class Meta:
        model = Product
        fields = '__all__'


class OpeningDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningDay
        fields = '__all__'