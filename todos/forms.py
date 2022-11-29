from django.forms import ModelForm
from todos.models import TodoItem, TodoList


class TodoListForm(ModelForm):
    class Meta:
        model = TodoList
        fields = "__all__"


class TodoItemForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = "__all__"
