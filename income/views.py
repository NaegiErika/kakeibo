from django.shortcuts import render

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Incomecategory, Income
from .forms import IncomeForm
from django.urls import reverse_lazy
import calendar
from django.db.models import Sum

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

#毎月支出の折れ線グラフとリスト
def income_analyse(request):
    #必要なデータを取得
    income_data = Income.objects.all()
    incomecategory_list =[]
    incomecategory_data = Incomecategory.objects.all().order_by('-incomecategory_name')
    #カテゴリの名前を取得
    for item in incomecategory_data:
        incomecategory_list.append(item.incomecategory_name)
    #日付ラベルの取得
    incomedate_list=[]
    for i in income_data:
        incomedate_list.append((i.incomedate.strftime('%Y/%m/%d')[:7]))
    #重複値を除外
    income_x_label = list(set(incomedate_list))
    income_x_label.sort(reverse=False)

    income_monthly_sum_data =[]
    #毎月ループ
    for i in range(len(income_x_label)):
        #毎月の初日と最終日を取得
        income_year,income_month = income_x_label[i].split("/")
        income_month_range = calendar.monthrange(int(income_year),int(income_month))[1]
        income_first_date = income_year + '-' + income_month +'-' + '01'
        income_last_date = income_year + '-' + income_month + '-' + str(income_month_range)
        #フィールダーで一か月分データを取得
        income_total_of_month = Income.objects.filter(incomedate__range=(income_first_date, income_last_date))
        #一か月カテゴリ毎の合計金額データセット
        income_category_total = income_total_of_month.values('incomecategory').annotate(income_total_price=Sum('incomemoney'))

        for j in range(len(income_category_total)):
            #一か月カテゴリ毎の合計金額を取得
            incomemoney = income_category_total[j]['income_total_price']
            incomecategory = Incomecategory.objects.get(pk=income_category_total[j]['incomecategory'])
            income_monthly_sum_data.append([income_x_label[i], incomecategory.incomecategory_name,incomemoney])

    #合計金額が0のデータセット処理
    income_matrix_list =[]
    for item_label in income_x_label:
        for item_category in incomecategory_list:
            income_matrix_list.append([item_label, item_category, 0])

    for yyyy_mm,category,total in income_monthly_sum_data:
        for i,data in enumerate(income_matrix_list):
            if data[0]==yyyy_mm and data[1] ==category:
                income_matrix_list[i][2] = total

    #折れ線のカラー設定
    border_color_list=['254,97,132,0.8','54,164,235,0.8','0,255,65,0.8','255,241,15,0.8',\
                       '255,94,25,0.8','84,77,203,0.8','204,153,50,0.8','214,216,165,0.8',\
                       '33,30,45,0.8','52,38,89,0.8']
    border_color =[]
    for x,y in zip(incomecategory_list, border_color_list):
        border_color.append([x,y])

    background_color_list=['254,97,132,0.5','54,164,235,0.5','0,255,65,0.5','255,241,15,0.5',\
                           '255,94,25,0.5','84,77,203,0.5','204,153,50,0.5','214,216,165,0.5'\
                           '33,30,45,0.5','52,38,89,0.5']

    background_color =[]
    for x,y in zip(incomecategory_list, background_color_list):
        background_color.append([x,y])

    #必要なデータをhtmlに渡す
    return render(request, 'income/income_analyse.html',{
        'income_x_label': income_x_label,
        'incomecategory_list': incomecategory_list,
        'border_color': border_color,
        'background_color': background_color,
        'income_matrix_list': income_matrix_list,
                 } )
