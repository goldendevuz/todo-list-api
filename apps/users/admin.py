from django.contrib import admin
from .models import User, UserConfirmation


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'phone_number', 'username', 'first_name', 'last_name']


admin.site.register(User, UserModelAdmin)
admin.site.register(UserConfirmation)