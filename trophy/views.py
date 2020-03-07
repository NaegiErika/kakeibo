from django.shortcuts import render
from django.views.generic import ListView
from trophy.models import Trophy
from expense.models import Expense, Expensecategory
from income.models import Income, Incomecategory
from wishing.models import Wishing
from django.db.models import Sum


def trophy_list(request):
    trophydata = Trophy.objects.filter(trophydone=False)
    incomecount = Income.objects.count()
    expensecount = Expense.objects.count()
    wishingdonecount = Wishing.objects.filter(wishingdone=True).count()
    if incomecount == 0:
        totalincome = 0
    else:
        totalincome = Income.objects.aggregate(Sum('incomemoney'))['incomemoney__sum']
    if expensecount == 0:
        totalexpense = 0
    else:
        totalexpense = Expense.objects.aggregate(Sum('expensemoney'))['expensemoney__sum']

    moneysaved = totalincome - totalexpense

    for item in trophydata:
        if item.pk == 1:
            if incomecount > 0:
                item.trophydone = True
                item.save()
        elif item.pk == 2:
            if expensecount > 0:
                item.trophydone = True
                item.save()
        elif item.pk == 3:
            if moneysaved > 0:
                item.trophydone = True
                item.save()
        elif item.pk == 4:
            if wishingdonecount > 0:
                item.trophydone = True
                item.save()
        elif item.pk == 5:
            if moneysaved > 10000:
                item.trophydone = True
                item.save()
        elif item.pk == 6:
            if moneysaved > 50000:
                item.trophydone = True
                item.save()
        elif item.pk == 7:
            if moneysaved > 100000:
                item.trophydone = True
                item.save()
        elif item.pk == 8:
            if moneysaved > 200000:
                item.trophydone = True
                item.save()
        elif item.pk == 9:
            if moneysaved > 1000000:
                item.trophydone = True
                item.save()
        elif item.pk == 10:
            if wishingdonecount >= 3:
                item.trophydone = True
                item.save()
        elif item.pk == 11:
            if wishingdonecount >= 5:
                item.trophydone = True
                item.save()
    trophyquery = Trophy.objects.all()
    trophyalldata = []
    for item in trophyquery:
        trophyalldata.append([item.pk, item.trophydone, item.trophycontent])
    return render(request, 'trophy/trophy_list.html', {'trophyalldata': trophyalldata} )

'''
class TrophyListView(ListView):
   model = Trophy
   template_name = 'trophy/trophy_list.html'

   def queryset(self):
       return Trophy.objects.all()'''
