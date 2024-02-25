from django.shortcuts import render
from players import mixins
from rest_framework import filters, generics
from django.contrib.auth.models import User
from users import serializers
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
    HTTP_200_OK
)
from django_filters import rest_framework as djangofilters
from rest_framework.response import Response
# Create your views here.
class UserDetailViewSet(generics.RetrieveUpdateDestroyAPIView):

    name = 'user-detail'
    queryset =  User.objects.all()
    serializer_class = serializers.UserSerializerDetail
    model = User


class UserViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializerDetail

    def get_object(self):
        return self.request.user
    
class ListUserViewSet(mixins.IsOwnerPeladaMixin, generics.ListAPIView):
    queryset = User.objects.all()
    filter_backends = (
        djangofilters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    search_fields = ('username',)
    serializer_class = serializers.ListUserSerializerDetail

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def create_user(request):
    new_user = serializers.UserSerializerDetail(data=request.data)
    if new_user.is_valid():
        user = new_user.create(request.data)
        user.set_password(request.data['password'])
        user.save()
        return Response({'message':'User {} created'.format(user.username)}, 
                                           status=HTTP_201_CREATED)
    else:
        return Response({'error': 'User not created'}, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response({'error': f'Please provide both username {username} and password {password}'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_400_BAD_REQUEST)
    
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key,
                    'user_name': user.username,
                    'user_email': user.email,
                    'user_id': user.id},
          status=HTTP_200_OK)

