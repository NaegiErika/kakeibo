from django.contrib import admin
from .models import Trophy

class TrophyAdmin(admin.ModelAdmin):
    list_display=('trophydone', 'trophycontent')

admin.site.register(Trophy)
