from django.contrib import admin
from .models import user,contact
# Register your models here.

class useradmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','mobile','gender','birth_date','address','image']
admin.site.register(user, useradmin)

class contactadmin(admin.ModelAdmin):
    list_display = ['name','email','message']
admin.site.register(contact, contactadmin)