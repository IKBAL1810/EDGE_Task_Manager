from django.urls import path
from .views import task_list, task_create, task_update, task_delete, toggle_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('update/<int:id>/', task_update, name='task_update'),
    path('delete/<int:id>/', task_delete, name='task_delete'),
    path('toggle-task/<int:id>/', toggle_task, name='toggle_task'),
]
