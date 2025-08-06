from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages

from .models import Category, Budget, Expense
from .forms import ExpenseForm


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


class ExpenseListView(generic.ListView):
    model = Expense
    context_object_name = 'expenses'
    template_name = 'expenses/expense_list.html'
    ordering = ('-created_at',)


@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, _('Expense successfully added'))
            return redirect('expenses:expense_list')
        else:
            messages.error(request, _('Invalid form'))
            return redirect('expenses:expense_list')
    else:
        form = ExpenseForm()
        return render(request, 'expenses/expense_form.html', {'form': form})

