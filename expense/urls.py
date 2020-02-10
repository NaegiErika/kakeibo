from django.urls import path
from . import views

app_name = 'expense'
urlpatterns = [
    path('expense_list/', views.ExpenseListView.as_view(), name='expense_list'),
    path('expense_create/', views.ExpenseCreateView.as_view(), name='expense_create'),
    path('expense_create_done/', views.expense_create_done, name='expense_create_done'),
    path('expense_update/<int:pk>/', views.ExpenseUpdateView.as_view(), name='expense_update'),
    path('expense_update_done/', views.expense_update_done, name='expense_update_done'),
    path('expense_delete/<int:pk>/', views.ExpenseDeleteView.as_view(), name='expense_delete'),
    path('expense_delete_done/', views.expense_delete_done, name='expense_delete_done'),
    path('expense_analyse/', views.expense_analyse, name='expense_analyse'),
    ]
