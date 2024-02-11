from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.core import validators
import re

# Create your models here.
class Jogador(models.Model):
    DIREITO, ESQUERDO = "D", "E"
    MELHOR_PE = (
        (DIREITO, ("Direito")),
        (ESQUERDO, ("Esquerdo")),
    )
    NOTA_CHOICES = tuple([(x, x) for x in range(1, 6)])
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, )
    email = models.EmailField('E-mail', unique=True, blank=True, null=True)
    rating = models.SmallIntegerField(verbose_name='Nota', choices=NOTA_CHOICES, default=3)
    organizacao = models.ForeignKey('Organizacao', related_name='jogadores', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Time(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    jogadores = models.ManyToManyField(Jogador, related_name='times')
    pelada = models.ForeignKey('Pelada', related_name='times', on_delete=models.CASCADE)


class Partida(models.Model):
    id = models.AutoField(primary_key=True)
    times = models.ManyToManyField("Time", related_name="partidas")
    vencedor = models.ForeignKey("Time", related_name="vencedor", on_delete=models.CASCADE)
    placar = models.CharField(max_length=10)


class CheckIn(models.Model):
    INDISPONIVEL, DISPONIVEL, NA_PELADA, FILA_DE_ESPERA = "I","D", "P", "F"
    STATUS = (
        (INDISPONIVEL, ("Disponivel")),
        (DISPONIVEL, ("Disponivel")),
        (NA_PELADA, ("Na pelada")),
        (FILA_DE_ESPERA, ("Removido")),
    )
    id = models.AutoField(primary_key=True)
    jogador = models.ForeignKey("Jogador", on_delete=models.CASCADE, related_name="status_partidas")
    status = models.CharField(max_length=1, choices=STATUS)
    partida = models.ForeignKey("Partida", on_delete=models.CASCADE, related_name="checkins")


class Organizacao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    administrador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='peladas')
    brasao = models.ImageField(upload_to='brasao/', blank=True, null=True)


class Pelada(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField()
    local = models.CharField(max_length=255)
    configuracao = models.OneToOneField("Configuracao", related_name="pelada", on_delete=models.CASCADE)
    organizacao = models.ForeignKey("Organizacao", related_name="peladas", on_delete=models.CASCADE)

    @property
    def create_times(self):
        if self.configuracao.tipo_sorteio == self.configuracao.ORDEM_CHEGADA:

            if self.times.all().count() == 0:
                qtd_jogadores = self.jogadores.all().filter(checkin__status="D").count()
                jogadores = self.jogadores.all().filter(checkin__status="D")
                qtd_por_time = self.configuracao.qtd_jogadores
                pelada = self
                time1 = Time.objects.create(nome="Time1", pelada=pelada)

                jogadores_time_1 = jogadores.order_by('?')[:int(qtd_por_time)]
                for jogador in jogadores_time_1:
                    time1.jogadores.add(jogador)
                    checkin = jogador.checkin
                    checkin.status = "P"
                    checkin.save()
                jogadores_time_2 = jogadores.filter(~Q(id__in=[o.id for o in jogadores_time_1]))
                time2 = Time.objects.create(nome="Time2", pelada=pelada)
                for jogador in jogadores_time_2:
                    time2.jogadores.add(jogador)
                    checkin = jogador.checkin
                    checkin.status = "P"
                    checkin.save()
                return True
            else:
                return False

class Configuracao(models.Model):
    QTD_JOGADORES = (
        ("5", "5 Jogadores"),
        ("6", "6 Jogadores"),
        ("7", "7 Jogadores"),
        ("8", "8 Jogadores"),
        ("9", "9 Jogadores"),
        ("10", "10 Jogadores"),
        ("11", "11 Jogadores"),
        ("12", "12 Jogadores"),
    )
    ORDEM_CHEGADA, SEM_SORTEIO, NIVEL_TECNICO = 'O', 'S', 'N'
    TIPO_SORTEIO = (
        (ORDEM_CHEGADA, "Ordem de chegada"),
        (SEM_SORTEIO, "Sem sorteio"),
        (NIVEL_TECNICO, "Nivel Tecnico")
    )
    id = models.AutoField(primary_key=True)
    qtd_jogadores = models.CharField(max_length=2, choices=QTD_JOGADORES)
    tipo_sorteio = models.CharField(max_length=1, choices=TIPO_SORTEIO)
