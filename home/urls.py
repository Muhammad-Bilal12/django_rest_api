from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name= 'home'),
    path('todo/', postTodo, name= 'todo'),
    path('get-todo', get_todo, name= 'get-todo'),
]