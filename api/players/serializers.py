from rest_framework import serializers
from users.serializers import AdminSerializerDetail
from .models import Organizacao, Configuracao, Jogador, Time, Pelada

from drf_writable_nested import WritableNestedModelSerializer 






class ConfiguracaoSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Configuracao
        fields = '__all__'

class OrganizacaoSerializers(serializers.ModelSerializer):
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


class PeladaSerializerDetail(serializers.ModelSerializer):
    jogadores = JogadoresSerializerDetail(many=True, read_only=True)
    # times = TimesSerializerDetail(many=True, read_only=True)
    # configuracao = ConfiguracaoSerializerDetail(many=False)
    admin = AdminSerializerDetail()

    class Meta:
        model = Organizacao
        exclude = ('configuracao',)
