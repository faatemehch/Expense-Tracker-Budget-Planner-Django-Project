from django import forms

from .models import Expense, Budget


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('amount', 'date', 'category', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ('amount', 'period', 'start_date', 'end_date', 'category',)
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }