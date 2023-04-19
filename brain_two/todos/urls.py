from django.urls import path
from todos.views import todo_list_list, todo_list_detail, create_list

urlpatterns = [
    path("", todo_list_list, name="todo_list_list"),
    path("<int:id>/", todo_list_detail, name="todo_list_detail"),
    path("todos/create/", create_list, name="create_list"),
]
