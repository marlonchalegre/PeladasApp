import jwt

from calendar import timegm
from datetime import datetime, timedelta

from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext as _
from rest_framework import serializers
from django.contrib.auth.models import User


class ListUserSerializerDetail(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username','email')

class UserSerializerDetail(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class AdminSerializerDetail(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email')
