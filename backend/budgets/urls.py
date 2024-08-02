from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BudgetViewSet, BudgetCategoryViewSet, BudgetTransactionViewSet

router = DefaultRouter()
router.register(r'budgets', BudgetViewSet)
router.register(r'budgets-categories', BudgetCategoryViewSet)
router.register(r'budgets-transactions', BudgetTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]