from django.contrib import admin

from expenses.models import Expense, Category, Budget


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user',)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'category', 'date', 'user', 'created_at', 'updated_at')


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'category', 'period', 'user', 'start_date', 'end_date')
