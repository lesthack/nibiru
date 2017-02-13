# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.utils.html import format_html
from .hacks import *
from .models import *

admin.site.unregister(User)

class itemForm(forms.ModelForm):
    class Meta:
        model = item
        exclude = ['created_at', 'updated_at', 'created_by', 'never_expire', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class':'vTextField', 'placeholder':'Name'}),
            'url': forms.TextInput(attrs={'class':'vTextField', 'placeholder':'Url'}),
            'username': forms.TextInput(attrs={'class':'vTextField', 'placeholder':'Username'}),
            'expire_at': forms.DateInput(attrs={'class':'vDateField', 'placeholder':'Expire'}),
            'password': forms.TextInput(attrs={'placeholder': 'Password', 'class':'vTextField'}),
        }

@admin.register(item)
class itemAdmin(nModelAdmin):
    list_display = ['id', 'sname', 'username', 'spassword', 'expire', 'stags', 'created_by']
    list_display_links = ['id']
    list_display_mobile = ['id', 'sname']
    search_fields = ['name', 'tag__name', 'url', 'username', 'password', 'comments', 'created_by__username']
    list_filter = ['expire_at', 'created_at']
    filter_horizontal = ('tag',)
    form = itemForm

    def get_queryset(self, request): 
        qs = super(itemAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(created_by=request.user)
        return qs
    
    def sname(self, obj):
        link = ''
        if obj.url.__len__() > 0:
            link = '<a href="{url}"><span class="fa fa-link"></span></a>'.format(url=obj.url)
        return format_html(u'<a href="/web/item/{id}/change/">{name}</a>&nbsp;{link}'.format(url=obj.url, name=obj.name, id=obj.id, link=link))
    sname.short_description = ''
    sname.allow_tags = True
    sname.admin_order_field = 'name'

    def expire(self, obj):
        if obj.expire_at:
            return '{}/{}/{}'.format(obj.expire_at.day, obj.expire_at.month, obj.expire_at.year)
        return 'Never'
    expire.short_description = 'Expire'
    expire.allow_tags = True
    expire.admin_order_field = 'expire_at'

    def spassword(self, obj):
        html = '''
        <div data-value="{password}" data-id="{id_password}" name="id-{id_password}" class="hide-show-password">
            <input id="{id_password}" type="text" readonly="readonly" class="password-value hide" value="******" onclick="copy2clipboard(this);"/>
            <a href="#id-{id_password}" class="eye" onclick="show_hide_pass(this);">
                <span id="eye-{id_password}" class="fa fa-eye"></span>
            </a>
        </div>
        '''.format(id_password=obj.id, password=obj.password)
        return format_html(html)
    spassword.short_description = 'Password'
    spassword.allow_tags = True

    def stags(self, obj):
        return format_html(' '.join(['<a href="?q={tag}">#{tag}</a>'.format(tag=t.name) for t in obj.tag.all()]))
    stags.short_description = 'Tags'
    stags.allow_tags = True

class tagForm(forms.ModelForm):
    class Meta:
        model = tag
        exclude = ['created_at', 'updated_at', 'created_by']

@admin.register(tag)
class tagAdmin(nModelAdmin):
    list_display = ['id', 'name', 'created_at','created_by', 'updated_at']
    list_display_links = ['id', 'name']
    list_display_mobile = ['id', 'name']
    search_fields = ['name', 'created_by__username']
    list_filter = ['created_by', 'created_at']
    form = tagForm

    def get_queryset(self, request): 
        qs = super(tagAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(created_by=request.user)
        return qs

@admin.register(User)
class userAdmin(nModelAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active_s', 'is_staff_s', 'is_superuser_s', 'last_login']
    list_display_links = ['id', 'username']
    list_display_mobile = ['id', 'username']
    search_fields = ['id', 'username', 'emai', 'first_name', 'last_name', 'last_login']
    list_filter = ['is_active', 'is_staff', 'is_superuser']

    def is_active_s(self, obj):
        if obj.is_active:
            return format_html('<span class="fa fa-check-square"/>')
        return ''
    is_active_s.short_description = 'Activo'
    is_active_s.allow_tags = True
    is_active_s.admin_order_field = 'is_active'

    def is_staff_s(self, obj):
        if obj.is_staff:
            return format_html('<span class="fa fa-check-square"/>')
        return ''
    is_staff_s.short_description = 'Estaff'
    is_staff_s.allow_tags = True
    is_staff_s.admin_order_field = 'is_staff'

    def is_superuser_s(self, obj):
        if obj.is_superuser:
            return format_html('<span class="fa fa-check-square"/>')
        return ''
    is_superuser_s.short_description = 'Admin'
    is_superuser_s.allow_tags = True
    is_superuser_s.admin_order_field = 'is_superuser'
