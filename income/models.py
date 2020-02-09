from django.db import models
from datetime import datetime

class Incomecategory(models.Model):
   class Meta:
       db_table ="incomecategory"
       verbose_name ="収入カテゴリ"
       verbose_name_plural ="収入カテゴリ"
   incomecategory_name = models.CharField(max_length=255,unique=True)
   def __str__(self):
       return self.incomecategory_name

class Income(models.Model):
   class Meta:
       db_table ="income"
       verbose_name ="収入"
       verbose_name_plural ="収入"

   incomedate = models.DateField(verbose_name="日付",default=datetime.now)
   incomecategory = models.ForeignKey(Incomecategory, on_delete = models.PROTECT, verbose_name="カテゴリ")
   incomemoney = models.IntegerField(verbose_name="金額", help_text="単位は日本円")
   incomememo = models.CharField(verbose_name="メモ", max_length=500)

   def __str__(self):
       return self.incomememo
