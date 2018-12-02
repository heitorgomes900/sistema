# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# Create your models here.
class Ocupacao(models.Model):
    Nome = models.CharField(max_length=250)
    Descricao = models.CharField(max_length=350)
    DescricaoLong = models.CharField(max_length=1000)
    Imagem = models.CharField(max_length=500)

    def __str__(self):
        return self.Nome + ' - ' + self.Descricao

    def get_absolute_url(self):
        return reverse('sistema/detalhes', kwargs={'pk': self.pk})

class Pessoa(models.Model):
    Ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=250)
    Telefone = models.CharField(max_length=100)
    Frequente = models.BooleanField(default=False)
    