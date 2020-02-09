from django.shortcuts import render

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Expensecategory, Expense
from .forms import ExpenseForm
from django.urls import reverse_lazy

class ExpenseListView(ListView):
   model = Expense
   template_name = 'expense/expense_list.html'

   def queryset(self):
       return Expense.objects.all()

class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    success_url = reverse_lazy('expense:expense_create_done')

def expense_create_done(request):
    return render(request, 'expense/expense_create_done.html')

class ExpenseUpdateView(UpdateView):
   model = Expense
   form_class = ExpenseForm
   success_url = reverse_lazy('expense:expense_update_done')

def expense_update_done(request):
    return render(request, 'expense/expense_update_done.html')

class ExpenseDeleteView(DeleteView):
    model = Expense
    success_url = reverse_lazy('expense:expense_delete_done')

def expense_delete_done(request):
    return render(request, 'expense/expense_delete_done.html')
