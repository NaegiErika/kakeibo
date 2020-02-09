from django.contrib import admin

# Register your models here.
from .models import Incomecategory, Income

class IncomeAdmin(admin.ModelAdmin):
    list_display=('incomedate','incomecategory','incomemoney','incomememo')

admin.site.register(Incomecategory)
admin.site.register(Income, IncomeAdmin)
