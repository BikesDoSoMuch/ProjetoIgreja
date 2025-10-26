from django.contrib import admin
from .models import Familia

admin.site.site_header = "Administração da Igreja"
admin.site.site_title = "Painel de Controle - Igreja"
admin.site.index_title = "Bem-vindo ao Painel de Famílias"

@admin.register(Familia)
class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('nome_responsavel', 'numero_pessoas', 'telefone', 'recebeu_ano_mes', 'data_cadastro')
    list_filter = ('recebeu_ano_mes', 'recebe_programas_sociais')
    search_fields = ('nome_responsavel', 'endereco', 'telefone')
    ordering = ('-data_cadastro',)
    
    fieldsets = (
        ("Informações Pessoais", {
            'fields': ('nome_responsavel', 'telefone', 'numero_pessoas', 'endereco')
        }),
        ("Informações Financeiras", {
            'fields': ('renda_mensal', 'recebeu_ano_mes', 'recebe_programas_sociais')
        }),
        ("Observações", {
            'fields': ('observacoes',)
        }),
    )


