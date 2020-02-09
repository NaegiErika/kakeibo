from django.shortcuts import render

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Incomecategory, Income
from .forms import IncomeForm
from django.urls import reverse_lazy

class IncomeListView(ListView):
   model = Income
   template_name = 'income/income_list.html'

   def queryset(self):
       return Income.objects.all()

class IncomeCreateView(CreateView):
    model = Income
    form_class = IncomeForm
    success_url = reverse_lazy('income:income_create_done')

def income_create_done(request):
    return render(request, 'income/income_create_done.html')

class IncomeUpdateView(UpdateView):
   model = Income
   form_class = IncomeForm
   success_url = reverse_lazy('income:income_update_done')

def income_update_done(request):
    return render(request, 'income/income_update_done.html')

class IncomeDeleteView(DeleteView):
    model = Income
    success_url = reverse_lazy('income:income_delete_done')

def income_delete_done(request):
    return render(request, 'income/income_delete_done.html')
