from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Familia
from .forms import FamiliaForm

class FamiliaListView(ListView):
    model = Familia
    template_name = 'familias/familia_list.html'
    context_object_name = 'familias'
    paginate_by = 20

class FamiliaCreateView(CreateView):
    model = Familia
    form_class = FamiliaForm
    template_name = 'familias/familia_form.html'
    success_url = reverse_lazy('familia_list')

class FamiliaUpdateView(UpdateView):
    model = Familia
    form_class = FamiliaForm
    template_name = 'familias/familia_form.html'
    success_url = reverse_lazy('familia_list')

class FamiliaDeleteView(DeleteView):
    model = Familia
    template_name = 'familias/familia_confirm_delete.html'
    success_url = reverse_lazy('familia_list')

class FamiliaDetailView(DetailView):
    model = Familia
    template_name = 'familias/familia_detail.html'
    context_object_name = 'familia'

import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def exportar_familias_csv(request):
   
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="familias.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nome', 'Endereço', 'Telefone', 'Nº Pessoas', 'Renda', 'Recebeu (AAAA-MM)', 'Observações', 'Data cadastro'])

    for f in Familia.objects.all().order_by('-data_cadastro'):
        writer.writerow([f.nome_responsavel, f.endereco, f.telefone, f.numero_pessoas, f.renda_mensal or '',
                         f.recebeu_ano_mes, f.observacoes, f.data_cadastro.strftime("%Y-%m-%d %H:%M")])
    return response



