from django.contrib import admin
from .models import Budget, BudgetCategory, BudgetTransaction


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'updated_at')
    search_fields = ('name', 'user__email')


@admin.register(BudgetCategory)
class BudgetCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'budget', 'limit', 'created_at', 'updated_at')
    search_fields = ('name', 'budget__name')


@admin.register(BudgetTransaction)
class BudgetTransactionAdmin(admin.ModelAdmin):
    list_display = ('budget_category', 'account', 'amount', 'transaction_type', 'created_at', 'updated_at')
    search_fields= ('budget_category__name', 'account__name', 'transaction_type')