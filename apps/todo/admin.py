from django.contrib import admin

from apps.shared.admin import BaseAdmin
from apps.todo.models import Todo

class TodoAdmin(BaseAdmin):
    list_display = [f.name for f in Todo._meta.fields]


admin.site.register(Todo, TodoAdmin)