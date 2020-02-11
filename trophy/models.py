from django.db import models

class Trophy(models.Model):
   class Meta:
       db_table ="trophy"
       verbose_name ="トロフィー"
       verbose_name_plural ="トロフィー"

   done = models.BooleanField(verbose_name="達成状況")
   content = models.CharField(verbose_name="内容", max_length=500)
