from django.db import models
from django.contrib.auth.models import User

class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

# python manage.py makemigrations main - put in terminal
# python manage.py migrate - apply the migrations
# python manage.py shell
# from main.models import Item, TodoList

# t = TodoList(name="todo List")
# t.save()
# TodoList.objects.all() - <QuerySet [<TodoList: todo List>]>
# TodoList.objects.get(id=1)
# TodoList.objects.get(name = "todo List")
# t.item_set.create(text="Shower bitch", complete = False)
# t.item_set.all() - get the items
