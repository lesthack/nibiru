# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class tag(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, blank=True, null=True)
    
    def __unicode__(self):
        return self.name

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
    category = models.ForeignKey(category, blank=True, null=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    never_expire = models.BooleanField(default=False)
    expire_at = models.DateField(blank=True, null=True)
    tag = models.ManyToManyField(tag)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.name
