from django.urls import path
from . import views

app_name = 'trophy'
urlpatterns = [
    path('trophy_list/', views.TrophyListView.as_view(), name='trophy_list'),
    ]
