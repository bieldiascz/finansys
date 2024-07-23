from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Transaction


@receiver(post_save, sender=Transaction) # Um decorador para conectar uma função aos sinais
def update_account_balance_on_save(sender, instance, created, **kwargs):
    account = instance.account
    if created:
        # Se a transação for nova
        if instance.transaction_type == 'income':
            account.balance += instance.amount
        elif instance.transaction_type == 'expense':
            account.balance -= instance.amount
    
    else:
        # se a transação for uma atualização
        previous_transaction = Transaction.objects.get(pk=instance.pk)
        
        # Remover o impacto da transação anterior
        if previous_transaction.transaction_type == 'income':
            account.balance -= previous_transaction.amount
        elif previous_transaction.transaction_type == 'expense':
            account.balance += previous_transaction.amount
            
        # Adicionar o impacto do novo valor
        if instance.transaction_type == 'income':
            account.balance += instance.amount
        elif instance.transaction_type == 'expense':
            account.balance -= instance.amount
    
    account.save()

@receiver(post_delete, sender=Transaction)
def update_account_balance_on_delete(sender, instance, **kwargs):
    # função para excluir uma transação
    account = instance.account
    
    if instance.transaction_type == 'income':
        account.balance -= instance.amount
    elif instance.transaction_type == 'expense':
        account.balance += instance.amount
    
    account.save()
