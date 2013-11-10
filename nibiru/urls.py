# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    ('^$', 'web.views.index'),
    url(r'^category/list/(?P<name_category>[a-zA-Z, ]+)/$', 'web.views.CategoryView'),
    url(r'^category/new/$', 'web.views.CategoryNewView'),    
    url(r'^item/new/$', 'web.views.ItemNewView'),
    url(r'^item/view/(\d+)/$', 'web.views.ItemShowView'),
    url(r'^item/edit/(\d+)/$', 'web.views.ItemEditView'),
    url(r'^item/delete/(\d+)/$', 'web.views.ItemDeleteView'),
    url(r'^auth/$', 'web.views.AuthView'),
    url(r'^logout/$', 'web.views.LogoutView'),
    url(r'^admin/', include(admin.site.urls)),    
)