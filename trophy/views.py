from django.shortcuts import render
from django.views.generic import ListView
from .models import Trophy

class TrophyListView(ListView):
   model = Trophy
   template_name = 'trophy/trophy_list.html'

   def queryset(self):
       return Trophy.objects.all()
