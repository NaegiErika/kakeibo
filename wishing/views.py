from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DeleteView
from wishing.models import Wishing
from django.urls import reverse_lazy
from wishing.forms import WishingForm
from expense.models import Expense, Expensecategory
import datetime

class WishingListView(ListView):
   model = Wishing
   template_name = 'wishing/wishing_list.html'

   def queryset(self):
       return Wishing.objects.all()

class WishingCreateView(CreateView):
    model = Wishing
    form_class = WishingForm
    success_url = reverse_lazy('wishing:wishing_create_done')

def wishing_create_done(request):
    return render(request, 'wishing/wishing_create_done.html')

class WishingDeleteView(DeleteView):
    model = Wishing
    success_url = reverse_lazy('wishing:wishing_delete_done')

def wishing_delete_done(request):
    return render(request, 'wishing/wishing_delete_done.html')

def wishing_done(request, pk):
    wishing = Wishing.objects.get(pk=pk)
    wishing.wishingdone = True
    wishing.save()
    #自動的にほしいものを支出データに登録
    new = Expense.objects.create(expensedate=datetime.date.today(), expensecategory=Expensecategory(pk=6), expensemoney=wishing.wishingmoney, expensememo=wishing.wishingmemo)
    new.save()
    return render(request, 'wishing/wishing_done.html')
