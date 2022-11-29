from django.shortcuts import render, redirect

from todos.models import TodoItem, TodoList
from todos.forms import TodoItemForm, TodoListForm


def todo_list_list(request):
    lists = TodoList.objects.all()
    context = {
        "lists": lists,
    }
    return render(request, "todo_lists/list.html", context)


def todo_list_detail(request, id):
    list = TodoList.objects.get(id=id)
    context = {
        "list": list,
    }
    return render(request, "todo_lists/detail.html", context)


def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            list = form.save()
            return redirect("todo_list_detail", id=list.id)
    else:
        form = TodoListForm()
    context = {
        "form": form,
    }
    return render(request, "todo_lists/create.html", context)


def todo_list_update(request, id):
    list = TodoList.objects.get(id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=list)
        if form.is_valid():
            list = form.save()
            return redirect("todo_list_detail", id=list.id)
    else:
        form = TodoListForm(instance=list)
    context = {
        "form": form,
    }
    return render(request, "todo_lists/update.html", context)


def todo_list_delete(request, id):
    if request.method == "POST":
        list = TodoList.objects.get(id=id)
        list.delete()
        return redirect("todo_list_list")
    return render(request, "todo_lists/delete.html")


def todo_item_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = TodoItemForm()
    context = {
        "form": form,
    }
    return render(request, "todo_items/create.html", context)


def todo_item_update(request, id):
    item = TodoItem.objects.get(id=id)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = TodoItemForm(instance=item)
    context = {
        "form": form,
    }
    return render(request, "todo_items/update.html", context)
