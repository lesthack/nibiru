# -*- coding: utf-8 -*-
from django import template
from datetime import datetime

register = template.Library()

@register.filter 
def get_attr(obj, val):
    return getattr(obj, val) 