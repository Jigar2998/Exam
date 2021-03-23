from django.contrib import admin
from .models import user
# Register your models here.

class useradmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','mobile','gender','birth_date','address','image']
admin.site.register(user, useradmin)