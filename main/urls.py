from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_List, name='task_list'),
    path('concluidas/', views.tasks_ok, name='tasks_ok'),
    path('pendentes', views.tasks_nok, name='tasks_nok'),
]