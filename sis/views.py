# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from .models import Ocupacao


def index(request):
    html = ''
    all_ocp = Ocupacao.objects.all()
    for ocp in all_ocp:
        url = '/sistema' + str(ocp.id) + '/'
    return HttpResponse("<h1>Página especial</h1>")

def detalhes(request, ocp_id):
    return HttpResponse("<h1>detalhes do id da ocupacao" + str(ocp_id) + "</h1>")