from django.contrib import admin
from .models import Task

@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','photo','date','name','roll','status']


