from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'transaction_type', 'description', 'created_at')  # Campos exibidos na lista de transações
    search_fields = ('account__name', 'description')  # Campos para busca
    list_filter = ('transaction_type', 'created_at')  # Filtros

admin.site.register(Transaction, TransactionAdmin)