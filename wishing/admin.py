from django.contrib import admin
from .models import Wishing

class WishingAdmin(admin.ModelAdmin):
    list_display=('wishingdone', 'wishingdate', 'wishingmoney','wishingmemo')

admin.site.register(Wishing)
