# -*- coding: utf-8 -*-
from django.contrib import admin
from web.models import *

class itemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'username', 'never_expire', 'expire_at', 'created_at', 'created_by']
    list_display_links = ['id','name']
    search_fields = ['name', 'category__name', 'url', 'username', 'password', 'comments', 'created_by__username']
    list_filter = ['category', 'expire_at', 'created_at']

class categoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at','created_by', 'updated_at']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'created_by__username']
    list_filter = ['created_by', 'created_at']

#admin.site.unregister(site)
admin.site.register(category, categoryAdmin)
admin.site.register(item, itemAdmin)
