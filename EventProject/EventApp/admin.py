from django.contrib import admin

# Register your models here.
from EventApp.models import *

class ChildAdmin(admin.ModelAdmin):
    list_display=['FirstName','FatherName','LastName','Age','Location_Where_You_Find']

class VolAdmin(admin.ModelAdmin):
    list_display=['FirstName','FatherName','LastName','Age']

class DonAdmin(admin.ModelAdmin):
    list_display=['Name',]



admin.site.register(DonDetail,DonAdmin)    
admin.site.register(ChildDetail,ChildAdmin)
admin.site.register(VolDetail,VolAdmin)
