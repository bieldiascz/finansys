from rest_framework import serializers
from .models import Budget, BudgetCategory, BudgetTransaction


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

class BudgetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetCategory
        fieds = '__all__'

class BudgetTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetTransaction
        fields = '__all__'