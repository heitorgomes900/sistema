# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Ocupacao(models.Model):
    Nome = models.CharField(max_length=250)
    Descricao = models.CharField(max_length=350)
    Imagem = models.CharField(max_length=500)


class Pessoa(models.Model):
    Ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=250)
    Descricao = models.CharField(max_length=100)
    