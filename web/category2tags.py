# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from Crypto.Cipher import AES
from web.models import *
import base64

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

def create_profiles():
    for user in User.objects.all():
        view_profile, created = profile.objects.get_or_create(user=user, use_crypt=False)
        if created:
            print 'created profile for', user
            view_profile.save()

def migrate_to_crypt():
    for user in User.objects.filter(profile__use_crypt=True):
        for view_item in item.objects.filter(created_by=user):
            old_password = view_item.password
            view_item.save()
            print 'change', old_password, 'to', view_item.password
