from django.contrib import admin
from django.urls import path,include

from todo_list_api import views
urlpatterns = [

    path("get_todo_list_api/",views.get_todo_list,name='get_todo_list'),
    path("save-task/",views.save_task,name='save_task'),
    path("get_task_data/",views.get_task,name="get_task")

]