from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls', namespace='polls')),
]
