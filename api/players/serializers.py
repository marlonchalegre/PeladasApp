from rest_framework import serializers
from users.serializers import AdminSerializerDetail
from .models import Organizacao, Configuracao, Jogador, Time, Pelada

from drf_writable_nested import WritableNestedModelSerializer
from drf_extra_fields.fields import Base64ImageField 

import base64
import logging

# logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class ConfiguracaoSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Configuracao
        fields = '__all__'


class OrganizacaoListSerializers(serializers.ModelSerializer):
    brasao = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Organizacao
        fields = '__all__'

    def get_brasao(self, organizacao):
        if organizacao.brasao.name:      
            img = open(organizacao.brasao.name, "rb") 
            data = img.read() 
            return "data:image/jpg;base64,%s" % base64.b64encode(data).decode("utf-8")
        
class OrganizacaoSerializers(serializers.ModelSerializer):
    brasao = Base64ImageField()
    class Meta:
        model = Organizacao
        fields = '__all__'


class PeladaSerializers(WritableNestedModelSerializer, serializers.ModelSerializer):
    configuracao = ConfiguracaoSerializerDetail()

    class Meta:
        model = Pelada
        fields = '__all__'

class JogadoresSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = '__all__'

class TimesSerializerDetail(serializers.ModelSerializer):
    jogadores = JogadoresSerializerDetail(many=True, read_only=True)

    class Meta:
        model = Time
        fields = '__all__'


class OrganizacaoSerializerDetail(OrganizacaoListSerializers):
    jogadores = JogadoresSerializerDetail(many=True, read_only=True)
    administrador = AdminSerializerDetail()
    peladas = PeladaSerializers(many=True, read_only=True)
