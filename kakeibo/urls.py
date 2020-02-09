from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    path('expense/', include('expense.urls')),
    path('income/', include('income.urls')),
]
