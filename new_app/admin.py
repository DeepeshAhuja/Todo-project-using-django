from django.contrib import admin

# Register your models here.
from new_app.models import TodoList

admin.site.register(TodoList)