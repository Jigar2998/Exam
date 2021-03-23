from django.contrib import admin
from .models import user,contact,task_assign
# Register your models here.

class useradmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','mobile','gender','birth_date','address','image']
admin.site.register(user, useradmin)

class contactadmin(admin.ModelAdmin):
    list_display = ['name','email','message']
admin.site.register(contact, contactadmin)

class task_assignadmin(admin.ModelAdmin):
    list_display = ['task_name','task_detail','assign_user','status','assign_work_date','due_date']
admin.site.register(task_assign, task_assignadmin)