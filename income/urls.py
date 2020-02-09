from django.urls import path
from . import views

app_name = 'income'
urlpatterns = [
    path('income_list/', views.IncomeListView.as_view(), name='income_list'),
    path('income_create/', views.IncomeCreateView.as_view(), name='income_create'),
    path('income_create_done/', views.income_create_done, name='income_create_done'),
    path('income_update/<int:pk>/', views.IncomeUpdateView.as_view(), name='income_update'),
    path('income_update_done/', views.income_update_done, name='income_update_done'),
    path('income_delete/<int:pk>/', views.IncomeDeleteView.as_view(), name='income_delete'),
    path('income_delete_done/', views.income_delete_done, name='income_delete_done'),
    ]
