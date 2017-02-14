# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from web.models import *

def item_view(request, item_id):
    try:
        view_item = item.objects.get(id=item_id)
    except item.DoesNotExist:
        raise Http404
    return render(request, 'ItemView.html', 
        {
            'item': view_item
        }
    )
