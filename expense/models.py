from django.db import models
from datetime import datetime

class Expensecategory(models.Model):
   class Meta:
       db_table ="expensecategory"
       verbose_name ="支出カテゴリ"
       verbose_name_plural ="支出カテゴリ"
   expensecategory_name = models.CharField(max_length=255,unique=True)
   def __str__(self):
       return self.expensecategory_name

class Expense(models.Model):
   class Meta:
       db_table ="expense"
       verbose_name ="支出"
       verbose_name_plural ="支出"

   expensedate = models.DateField(verbose_name="日付",default=datetime.now)
   expensecategory = models.ForeignKey(Expensecategory, on_delete = models.PROTECT, verbose_name="カテゴリ")
   expensemoney = models.IntegerField(verbose_name="金額", help_text="単位は日本円")
   expensememo = models.CharField(verbose_name="メモ", max_length=500)

   def __str__(self):
       return self.expensememo
