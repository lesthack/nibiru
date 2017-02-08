# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url('', include('social_django.urls', namespace='social')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
