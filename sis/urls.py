from django.conf.urls import url
from . import views

app_name = 'sistema'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<ocp_id>[0-9]+)/$', views.detalhes, name='detalhes'), # ^ = inicio; $ = fim; (?P<>) = indica parametro; [0-9]+ = range numerico
    #url(r'ocp/add/$', views.OcupacaoCreate.as_view(), name='ocp-add'),
    url(r'^(?P<ocp_id>[0-9]+)/frequente$', views.frequente, name='frequente')
]