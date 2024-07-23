from django.db import models
from accounts.models import Account


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    transaction_type = models.CharField(max_length=10, choices=(('income', 'Income'), ('expense', 'Expense')))
    description = models.CharField(max_length=259)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.account.user.username} - {self.account.name} - {self.amount} ({self.transaction_type})'