from django.db import models

class Familia(models.Model):
    nome_responsavel = models.CharField("Nome do responsável", max_length=200)
    endereco = models.CharField("Endereço", max_length=300, blank=True)
    telefone = models.CharField("Telefone", max_length=30, blank=True)
    numero_pessoas = models.PositiveIntegerField("Número de pessoas", default=1)
    renda_mensal = models.DecimalField("Renda mensal (R$)", max_digits=10, decimal_places=2, null=True, blank=True)
    recebe_programas_sociais = models.BooleanField("Recebe programas sociais?", default=False)
    observacoes = models.TextField("Observações", blank=True)
    data_cadastro = models.DateTimeField("Data do cadastro", auto_now_add=True)
    recebeu_ano_mes = models.CharField("Recebeu em (AAAA-MM)", max_length=7, blank=True,
                                       help_text="Use formato 2025-10 para registrar mês/ano da última entrega")

    def __str__(self):
        return f"{self.nome_responsavel} — {self.numero_pessoas} pessoas"

