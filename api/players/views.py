from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView
from rest_framework.decorators import action


from players import mixins
from .models import Organizacao, Configuracao, Jogador, Time
from . import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import generics, status, viewsets, exceptions
from players import permissions
from .permissions import PublicEndpoint, IsOwnerPelada
from rest_framework import filters
from django_filters import rest_framework as djangofilters
from rest_framework import viewsets, authentication, permissions

from django.http import JsonResponse

from django.conf import settings
import logging

fmt = getattr(settings, 'LOG_FORMAT', None)
lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)

logging.basicConfig(format=fmt, level=lvl)

# Create your views here.

class OrganizacaoViewSet(mixins.FilteringAndOrderingMixin, generics.ListCreateAPIView ):

    permission_classes = (PublicEndpoint,)
    name = 'pelada-list'
    serializer_class = serializers.OrganizacaoSerializers
    model = Organizacao
    filter_fields = ('administrador__username',)
    search_fields = ('nome',)
    queryset = Organizacao.objects.all()


class OrganizacaoDetailViewSet(mixins.IsOwnerPeladaMixin,  generics.RetrieveUpdateDestroyAPIView):

    name = 'organizacao-detail'
    queryset =  Organizacao.objects.all()
    serializer_class = serializers.OrganizacaoSerializerDetail
    model = Organizacao

class JogadorDetailViewSet(mixins.IsPeladaMixin,generics.RetrieveUpdateDestroyAPIView):

    name = 'jogador-detail'
    queryset =  Jogador.objects.all()
    serializer_class = serializers.JogadoresSerializerDetail
    model = Jogador

class TimeDetailViewSet(mixins.IsPeladaMixin,generics.RetrieveUpdateDestroyAPIView):

    name = 'times-detail'
    queryset =  Time.objects.all()
    serializer_class = serializers.TimesSerializerDetail
    model = Time

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        jogadores = instance.jogadores.all()
        for jogador in jogadores:
            checking = jogador.checkin
            checking.status = "D"
            checking.save()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class PeladaConfiguracaoDetailViewSet(generics.RetrieveUpdateDestroyAPIView):

    name = 'configuracao-pelada-detail'
    queryset =  Organizacao.objects.all()
    serializer_class = serializers.ConfiguracaoSerializerDetail
    model = Organizacao

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        configuracao = instance.configuracao
       
        return Response(status=status.HTTP_200_OK,data=serializers.ConfiguracaoSerializerDetail(configuracao,context={'request': request}).data)

class ConfiguracaoDetailViewSet(mixins.IsPeladaMixin,generics.RetrieveUpdateDestroyAPIView):

    name = 'configuracao-detail'
    queryset =  Configuracao.objects.all()
    serializer_class = serializers.ConfiguracaoSerializerDetail
    model = Configuracao

class TimeList(generics.ListCreateAPIView, generics.RetrieveDestroyAPIView):

    serializer_class = serializers.TimesSerializerDetail
    queryset =  Time.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        user = self.request.user
        times = Time.objects.filter(pelada__admin=user)
        return Response(status=status.HTTP_200_OK,
                        data=serializers.TimesSerializerDetail(times, many=True, context={'request': request}).data)


class ConfiguracaoList(generics.ListCreateAPIView):

    serializer_class = serializers.ConfiguracaoSerializerDetail
    queryset =  Configuracao.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if request.user.is_anonymous:
             return Response(status=status.HTTP_401_UNAUTHORIZED,
                        data=({"Warning": "Voce nao esta autenticado"}))
        else:
            user = self.request.user
            configuracoes = Configuracao.objects.filter(pelada__admin=user)
        return Response(status=status.HTTP_200_OK,
                        data=serializers.ConfiguracaoSerializerDetail(configuracoes, many=True, context={'request': request}).data)

class JogadoresList(generics.ListAPIView):
    filter_backends = (
        djangofilters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    search_fields = ('nome',)
    serializer_class = serializers.JogadoresSerializerDetail
    queryset =  Jogador.objects.all()

    # def get(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     user = self.request.user
    #     queryset = queryset.filter(nome__icontains=user)
    #     page = self.paginate_queryset(queryset)

    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

class OrganizacaoListUser(generics.ListCreateAPIView):
    authentication = (authentication.SessionAuthentication)
    serializer_class = serializers.OrganizacaoListSerializers
    queryset = Organizacao.objects.all()
    
    def list(self, request, *args, **kwargs):
        if request.user.is_anonymous:
             return Response(status=status.HTTP_401_UNAUTHORIZED,
                        data=({"Warning": "Voce nao esta autenticado"}))
        else:
            user = self.request.user
            organizacoes = Organizacao.objects.filter(administrador=user)
        return Response(status=status.HTTP_200_OK,
                        data=serializers.OrganizacaoListSerializers(organizacoes, many=True, context={'request': request}).data)



    def validate(self, data):
        errors = {}
        admin = data.get('administrador')

        if self.request.user != admin:
            errors['error'] = 'O usuario não pode criar'
            raise serializers.ValidationError(errors)

        return data

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)


class CreateTimes(viewsets.ViewSet):

    @action(detail=True, methods=['post'])
    def create_times(self, request, pk=None):
            pelada = self.get_queryset().get(pk=pk)
            if pelada.create_times == True:
                return Response({"status":"Times criados"},status=status.HTTP_200_OK)
            if pelada.create_times == False:
                return Response({"status":"Times ja criados ou sua solicitacao possui erro"},status=status.HTTP_401_UNAUTHORIZED)

    def get_queryset(self):
        qs = Organizacao.objects.all()
        return qs
