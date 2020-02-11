from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('admin/', admin.site.urls),
    path('expense/', include('expense.urls')),
    path('income/', include('income.urls')),
    path('wishing/', include('wishing.urls')),
    path('trophy/', include('trophy.urls')),
]
