from rest_framework import viewsets
from .models import Budget, BudgetCategory, BudgetTransaction
from .serializers import BudgetSerializer, BudgetCategorySerializer, BudgetTransactionSerializer


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

class BudgetCategoryViewSet(viewsets.ModelViewSet):
    queryset = BudgetCategory.objects.all()
    serializer_class = BudgetCategorySerializer

class BudgetTransactionViewSet(viewsets.ModelViewSet):
    queryset = BudgetTransaction.objects.all()
    serializer_class = BudgetTransactionSerializer

    