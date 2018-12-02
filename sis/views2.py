from django.views import generic
from .models import Ocupacao
from django.views.generic.edit import CreateView, UpdateView, DeleteView
class IndexView(generic.ListView):
    template_name = 'sistema/index.html'
    context_object_name = 'all_ocp'
    def get_queryset(self):
        return Ocupacao.objects.all()

class DetalhesView(generic.DetailView):
    model = Ocupacao
    template_name = 'sistema/detalhes.html'
    
class OcupacaoCreate(CreateView):
    model = Ocupacao
    fields = ['Nome','Descricao','Imagem']
    template_name = 'sistema/ocp_form.html'