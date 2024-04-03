from django.contrib import admin
from django.http.request import HttpRequest
from.models import Advertising,Groups

class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ['id', ]
    list_display_links = ['id',]
admin.site.register(Advertising,AdvertisingAdmin)

class GroupsAdmin(admin.ModelAdmin):
    list_display= ['id','name', 'groups']
    list_display_links = ['id','name','groups']

admin.site.register(Groups,GroupsAdmin)

 