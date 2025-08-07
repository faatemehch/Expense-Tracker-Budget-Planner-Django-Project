from django.urls import path

from . import views

app_name = 'expenses'

urlpatterns = [
    path('expenses/dashboard/', views.dashboard, name='dashboard'),
    path('expenses/add/', views.add_expense, name='expense_add'),

    path('expenses/list/', views.ExpenseListView.as_view(), name='expense_list'),
    path('exoenses/<int:pk>/delete/', views.ExpenseDeleteView.as_view(), name='expense_delete'),
    path('exoenses/<int:pk>/update/', views.ExpenseUpdateView.as_view(), name='expense_update'),
]