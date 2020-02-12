from django.db import models
from datetime import datetime

class Wishing(models.Model):
   class Meta:
       db_table ="wishing"
       verbose_name ="ほしいもの"
       verbose_name_plural ="ほしいもの"

   wishingdate = models.DateField(verbose_name="日付",default=datetime.now)
   wishingmoney = models.IntegerField(verbose_name="金額", help_text="単位は日本円")
   wishingmemo = models.CharField(verbose_name="メモ", max_length=500)
   wishingdone = models.BooleanField(default=False, verbose_name="達成状況")

   def __str__(self):
       return self.wishingmemo
