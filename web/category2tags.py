# -*- coding: utf-8 -*-
from django.shortcuts import render
from web.models import *

def migrate_category_tags():
    """
        Migración de categorias a tags
    """

    for c in category.objects.all():
        tag_new, created = tag.objects.get_or_create(name=c.name, created_by=c.created_by)
        if created:
            tag_new.save()
            print 'created', tag_new, 'tag'
    
    for i in item.objects.all():
        if i.category:
            ct = tag.objects.get(name=i.category, created_by=i.created_by)
            if i.tag.filter(id=ct.id).count() == 0:
                i.tag.add(ct)
                print 'tag',ct,'added.'

    return 'ok'
