from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import generic

from .models import Category, Budget, Expense
from .forms import ExpenseForm, BudgetForm


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


# --------------- Expenses View ---------------
class ExpenseListView(generic.ListView):
    model = Expense
    context_object_name = 'expenses'
    template_name = 'expenses/expense_list.html'
    ordering = ('-created_at',)

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        startDate = self.request.GET.get('startDate')
        endDate = self.request.GET.get('endDate')
        if startDate and endDate:
            queryset = queryset.filter(date__range=(startDate, endDate))
        return queryset


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


class ExpenseDeleteView(generic.DeleteView):
    model = Expense

    # success_url = reverse_lazy('expenses:expense_list')
    # success_message = "Expense was deleted successfully"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_success_url(self):
        messages.success(self.request, _("Expense deleted successfully"))
        return reverse_lazy('expenses:expense_list')


class ExpenseUpdateView(generic.UpdateView):
    model = Expense
    fields = ('amount', 'date', 'category', 'description')
    template_name = 'expenses/expense_form.html'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_success_url(self):
        messages.success(self.request, _("Expense updated successfully"))
        return reverse_lazy('expenses:expense_list')


# --------------- Budget View ---------------

class BudgetListView(generic.ListView):
    model = Budget
    template_name = 'expenses/budget_list.html'
    context_object_name = 'budgets'
    paginate_by = 10
    ordering = ('-start_date',)


class AddNewBudget(LoginRequiredMixin, generic.CreateView):
    model = Budget
    form_class = BudgetForm
    success_url = reverse_lazy('expenses:budget_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BudgetDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Budget

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_success_url(self):
        messages.success(self.request, _("Budget updated successfully"))
        return reverse_lazy('expenses:budget_list')


class BudgetUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Budget
    fields = ('amount', 'period', 'start_date', 'end_date', 'category',)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_success_url(self):
        messages.success(self.request, _("Budget updated successfully"))
        return reverse_lazy('expenses:budget_list')

