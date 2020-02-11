from django.contrib import admin
from .models import Trophy

class TrophyAdmin(admin.ModelAdmin):
    list_display=('done', 'content')

admin.site.register(Trophy)
