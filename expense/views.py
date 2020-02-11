from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Expensecategory, Expense
from .forms import ExpenseForm
from django.urls import reverse_lazy
import calendar
from django.db.models import Sum

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

#毎月支出の折れ線グラフとリスト
def expense_analyse(request):
    #必要なデータを取得
    expense_data = Expense.objects.all()
    expensecategory_list =[]
    expensecategory_data = Expensecategory.objects.all().order_by('-expensecategory_name')
    #カテゴリの名前を取得
    for item in expensecategory_data:
        expensecategory_list.append(item.expensecategory_name)
    #日付ラベルの取得
    expensedate_list=[]
    for i in expense_data:
        expensedate_list.append((i.expensedate.strftime('%Y/%m/%d')[:7]))
    #重複値を除外
    expense_x_label = list(set(expensedate_list))
    expense_x_label.sort(reverse=False)


    expense_monthly_sum_data =[]
    #毎月ループ
    for i in range(len(expense_x_label)):
        #毎月の初日と最終日を取得
        expense_year,expense_month = expense_x_label[i].split("/")
        expense_month_range = calendar.monthrange(int(expense_year),int(expense_month))[1]
        expense_first_date = expense_year + '-' + expense_month +'-' + '01'
        expense_last_date = expense_year + '-' + expense_month + '-' + str(expense_month_range)
        #フィールダーで一か月分データを取得
        expense_total_of_month = Expense.objects.filter(expensedate__range=(expense_first_date, expense_last_date))
        #一か月カテゴリ毎の合計金額データセット
        expense_category_total = expense_total_of_month.values('expensecategory').annotate(expense_total_price=Sum('expensemoney'))

        for j in range(len(expense_category_total)):
            #一か月カテゴリ毎の合計金額を取得
            expensemoney = expense_category_total[j]['expense_total_price']
            expensecategory = Expensecategory.objects.get(pk=expense_category_total[j]['expensecategory'])
            expense_monthly_sum_data.append([expense_x_label[i], expensecategory.expensecategory_name,expensemoney])

    #合計金額が0のデータセット処理
    expense_matrix_list =[]
    for item_label in expense_x_label:
        for item_category in expensecategory_list:
            expense_matrix_list.append([item_label, item_category, 0])

    for yyyy_mm,category,total in expense_monthly_sum_data:
        for i,data in enumerate(expense_matrix_list):
            if data[0]==yyyy_mm and data[1] ==category:
                expense_matrix_list[i][2] = total

    #折れ線のカラー設定
    border_color_list=['254,97,132,0.8','54,164,235,0.8','0,255,65,0.8','255,241,15,0.8',\
                       '255,94,25,0.8','84,77,203,0.8','204,153,50,0.8','214,216,165,0.8',\
                       '33,30,45,0.8','52,38,89,0.8']
    border_color =[]
    for x,y in zip(expensecategory_list, border_color_list):
        border_color.append([x,y])

    background_color_list=['254,97,132,0.5','54,164,235,0.5','0,255,65,0.5','255,241,15,0.5',\
                           '255,94,25,0.5','84,77,203,0.5','204,153,50,0.5','214,216,165,0.5'\
                           '33,30,45,0.5','52,38,89,0.5']

    background_color =[]
    for x,y in zip(expensecategory_list, background_color_list):
        background_color.append([x,y])

    #必要なデータをhtmlに渡す
    return render(request, 'expense/expense_analyse.html',{
        'expense_x_label': expense_x_label,
        'expensecategory_list': expensecategory_list,
        'border_color': border_color,
        'background_color': background_color,
        'expense_matrix_list': expense_matrix_list,
                 } )
