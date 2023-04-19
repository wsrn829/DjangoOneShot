from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem


# Create your views here.
def todo_list_list(request):
    todos = TodoList.objects.all()
    context = {
        "todo_list": todos,
    }
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    todo = get_object_or_404(TodoItem, id=id)
    context = {
        "todo_object": todo,
    }
    return render(request, "todos/detail.html", context)
