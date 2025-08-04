from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required

from .models import Category, Budget, Expense


@login_required
def dashboard(request):
    user = request.user
    expenses = Expense.objects.filter(user=user)
    budgets = Budget.objects.filter(user=user)
    context = {
        'expenses': expenses,
        'budgets': budgets,
    }
    return render(request, 'expenses/dashboard.html', context)