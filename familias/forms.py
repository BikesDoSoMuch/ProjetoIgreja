from django import forms
from .models import Familia

class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = ['nome_responsavel','endereco','telefone','numero_pessoas','renda_mensal',
                  'recebe_programas_sociais','observacoes','recebeu_ano_mes']
