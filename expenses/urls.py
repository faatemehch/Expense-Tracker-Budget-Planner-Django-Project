from django.urls import path

from . import views

app_name = 'expenses'

urlpatterns = [
    path('expenses/dashboard/', views.dashboard, name='dashboard'),
    path('expenses/add/', views.add_expense, name='add_expense'),

    path('expenses/list/', views.ExpenseListView.as_view(), name='expense_list'),
]