from django.urls import path, include
from todoApp import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:id>', views.todo_detail, name='todo_detail'),
    path('new', views.todo_new, name='todo_new'),
    path('<int:id>/edit', views.todo_edit, name='todo_edit'),
    path('<int:id>/delete', views.todo_delete, name='todo_delete'),
]