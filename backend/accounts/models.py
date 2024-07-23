from django.db import models
from django.conf import settings


class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Usa uma chave estrangeira para conectar com os models da aplicação users
    name = models.CharField(max_length=255) # nome da conta bancária
    balance = models.DecimalField(max_digits=15, decimal_places=2) # Saldo da conta
    created_at = models.DateTimeField(auto_now_add=True) # data que a conta tá criada
    
    def __str__(self):
        return f'{self.user.username} - {self.name} - {self.balance}'