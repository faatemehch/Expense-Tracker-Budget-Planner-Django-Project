from django.urls import path

from . import views

app_name = 'expenses'

urlpatterns = [
    # Expenses
    path('expenses/dashboard/', views.dashboard, name='dashboard'),
    path('expenses/add/', views.add_expense, name='expense_add'),
    path('expenses/', views.ExpenseListView.as_view(), name='expense_list'),
    path('exoenses/<int:pk>/delete/', views.ExpenseDeleteView.as_view(), name='expense_delete'),
    path('exoenses/<int:pk>/update/', views.ExpenseUpdateView.as_view(), name='expense_update'),
    # Budgets
    path('budgets/', views.BudgetListView.as_view(), name='budget_list'),
    path('budget/add/', views.AddNewBudget.as_view(), name='budget_add'),
    path('budgets/<int:pk>/delete/', views.BudgetDeleteView.as_view(), name='budget_delete'),
    path('budgets/<int:pk>/update/', views.BudgetUpdateView.as_view(), name='budget_update'),
]