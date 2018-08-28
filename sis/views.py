# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Ocupacao
from django.http import Http404

def index(request):
    all_ocp = Ocupacao.objects.all()
    #template = loader.get_template('sistema/index.html')

    context = {
        'all_ocp':all_ocp, 
    }

    return render(request, 'sistema/index.html', context)
    
    #Usar templates
    #html = ''
    #url = '/sistema' + str(ocp.id) + '/'
    #for ocp in all_ocp:
    #    html += '<a href="' + url +'">' + ocp.Nome + '</a><br>'

def detalhes(request, ocp_id):
    '''try:
        ocp = Ocupacao.objects.get(pk=ocp_id)
    except Ocupacao.DoesNotExist: 
        raise Http404('Não existe esta ocupação!')'''
    ocp = get_object_or_404(Ocupacao, pk=ocp_id)
    return render(request, 'sistema/detalhes.html', {'ocp':ocp})
    #return HttpResponse("<h1>detalhes do id da ocupacao" + str(ocp_id) + "</h1>")

def frequente(request):
    