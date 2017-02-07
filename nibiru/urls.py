# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url('', include('social_django.urls', namespace='social')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^', admin.site.urls),
]
