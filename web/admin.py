# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.utils.html import format_html
from web.models import *

class nModelAdmin(admin.ModelAdmin):
    """
       Overwrite 
    """
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.save()

class itemForm(forms.ModelForm):
    class Meta:
        model = item
        exclude = ['created_at', 'updated_at', 'created_by', 'never_expire', 'category']
        widgets = {
            'url': forms.TextInput(attrs={'class':'vTextField'}),
            'password': forms.PasswordInput(attrs={})
        }

@admin.register(item)
class itemAdmin(nModelAdmin):
    list_display = ['id', 'name', 'username', 'spassword', 'expire', 'created_by']
    list_display_links = ['id','name']
    search_fields = ['name', 'category__name', 'url', 'username', 'password', 'comments', 'created_by__username']
    list_filter = ['expire_at', 'created_at']
    filter_horizontal = ('tag',)
    form = itemForm

    def get_queryset(self, request): 
        qs = super(itemAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(created_by=request.user)
        return qs

    def expire(self, obj):
        if obj.expire_at:
            return '{}/{}/{}'.format(obj.expire_at.day, obj.expire_at.month, obj.expire_at.year)
        return 'Never'
    expire.short_description = 'Expire'
    expire.allow_tags = True
    expire.admin_order_field = 'expire_at'

    def spassword(self, obj):
        return '****'
    spassword.short_description = 'Password'
    spassword.allow_tags = True

class tagForm(forms.ModelForm):
    class Meta:
        model = tag
        exclude = ['created_at', 'updated_at', 'created_by']

@admin.register(tag)
class tagAdmin(nModelAdmin):
    list_display = ['id', 'name', 'created_at','created_by', 'updated_at']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'created_by__username']
    list_filter = ['created_by', 'created_at']
    form = tagForm

    def get_queryset(self, request): 
        qs = super(tagAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(created_by=request.user)
        return qs
