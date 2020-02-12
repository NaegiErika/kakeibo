from django.urls import path
from . import views

app_name = 'wishing'
urlpatterns = [
    path('wishing_list/', views.WishingListView.as_view(), name='wishing_list'),
    path('wishing_create/', views.WishingCreateView.as_view(), name='wishing_create'),
    path('wishing_create_done/', views.wishing_create_done, name='wishing_create_done'),
    path('wishing_delete/<int:pk>/', views.WishingDeleteView.as_view(), name='wishing_delete'),
    path('wishing_delete_done/', views.wishing_delete_done, name='wishing_delete_done'),
    path('wishing_done/<int:pk>/', views.wishingdone, name='wishing_done'),
    ]
