from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'balance', 'created_at')


admin.site.register(Account, AccountAdmin)
