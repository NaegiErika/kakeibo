from django.db import models

class Trophy(models.Model):
   class Meta:
       db_table ="trophy"
       verbose_name ="トロフィー"
       verbose_name_plural ="トロフィー"

   trophydone = models.BooleanField(verbose_name="達成状況")
   trophycontent = models.CharField(verbose_name="内容", max_length=500)
