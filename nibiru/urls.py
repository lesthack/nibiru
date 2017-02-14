# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib import admin
from web.views import *

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/web/item/')),
    url(r'^web/item/(?P<item_id>\d+)/view/', admin.site.admin_view(item_view)),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
