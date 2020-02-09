from django.contrib import admin

# Register your models here.
from .models import Expensecategory, Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display=('expensedate','expensecategory','expensemoney','expensememo')

admin.site.register(Expensecategory)
admin.site.register(Expense, ExpenseAdmin)
