from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add/', views.add_task, name='add_task'),
]
