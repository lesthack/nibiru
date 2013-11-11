# -*- coding: utf-8 -*-
from django.forms import *
from django import forms
from web.models import *

class itemForm(ModelForm):
    password_rep = forms.CharField(widget=forms.TextInput)

    def __init__(self, user, *args, **kargs):
        super(itemForm, self).__init__(*args, **kargs)
        self.user = user
        self.fields['category'].queryset = category.objects.filter(created_by=self.user)

    class Meta:
        model = item
        fields = [
            "name", "url", "category", "username", "password", "never_expire", "expire_at", "comments"
        ]
        widgets = {
            "name": TextInput(attrs={'placeholder': 'Name Item', 'class':'form-control input-block-level'}),
            "url": TextInput(attrs={'placeholder': 'http://', 'class':'form-control input-block-level'}),
            "username": TextInput(attrs={'placeholder': 'Username', 'class':'form-control input-block-level'}),
            "password": TextInput(attrs={'placeholder': 'Password', 'class':'form-control input-block-level'}),
            "category": Select(attrs={'class':'form-control input-block-level'}),
            "comments": Textarea(attrs={'placeholder':'Comments', 'class':'form-control input-block-level', 'rows':'4'}),
            "expire_at": TextInput(attrs={'placeholder':'Date Expire', 'class':'datepicker'}),
        }    

    def clean(self):
        cleaned_data = super(itemForm, self).clean()

        cpassword = cleaned_data.get("password")
        cpasswordrep = cleaned_data.get("password_rep")
        cnever_expire = cleaned_data.get("never_expire")
        cexpire_at =cleaned_data.get("expire_at")

        if cpassword != cpasswordrep:
            msg = u"The passwords is not equals. "
            self._errors["password"] = self.error_class([msg])

        if cnever_expire == False and cexpire_at == None:
            msg = u"Date field is required."
            self._errors["expire_at"] = self.error_class([msg])

        return cleaned_data

class categoryForm(ModelForm):
    def __init__(self, user, *args, **kargs):
        super(categoryForm, self).__init__(*args, **kargs)
        self.user = user

    class Meta:
        model = category
        fields = [
            "name"
        ]
        widgets = {
            "name": TextInput(attrs={'placeholder': 'Name Category', 'class':'form-control input-block-level'}),
        }    

    def clean(self):
        cleaned_data = super(categoryForm, self).clean()

        cname = cleaned_data.get("name")
        if category.objects.filter(created_by=self.user,name=cname).count() > 0 or cname.lower() == 'all':
            msg = u"The name already exists. "
            self._errors["name"] = self.error_class([msg])

        return cleaned_data