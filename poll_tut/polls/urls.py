from django.urls import path, include
from . import views

app_name = "polls"
urlpatterns = [
    path('list/', views.poll_list, name='list'),
    path('<int:poll_id>/', views.poll_detail, name='details'),
]