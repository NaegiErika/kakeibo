from django.urls import path
from . import views

app_name = 'trophy'
urlpatterns = [
    path('trophy_list/', views.trophy_list, name='trophy_list'),
    ]
