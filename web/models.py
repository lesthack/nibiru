# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.name

class item(models.Model):
    name = models.CharField(max_length=254)
    url = models.TextField(blank=True, null=True)
    category = models.ForeignKey(category)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    never_expire = models.BooleanField()
    expire_at = models.DateField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.name