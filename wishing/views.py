from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DeleteView
from .models import Wishing
from django.urls import reverse_lazy
from .forms import WishingForm
from expense.models import Expense, Expensecategory
from datetime import datetime

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
    '''自動的に支出新規データ登録したいが、うまくいかず
    new = Expense()
    new.expensedate = datetime.now()
    new.expensecategory = Expense.expensecategory[5]
    new.expensememo = wishing.wishingmemo
    new.expensemoney = wishing.wishingmoney
    new.save()
    '''
    return render(request, 'wishing/wishing_done.html')
