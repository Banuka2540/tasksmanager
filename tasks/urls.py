from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('registation/logged_out', views.login, name='logged_out'),
]
