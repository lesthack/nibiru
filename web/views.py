# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader, Context
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from web.models import *
from web.forms import *

nitems = 10

@login_required(login_url='/auth')
def index(request):		
	return HttpResponseRedirect('/category/list/all/')


@login_required(login_url='/auth')
def ItemNewView(request):		
	alert = None

	if request.method == "POST":
		formItem = itemForm(request.user, request.POST)
		if formItem.is_valid():
			new_item = formItem.save(commit=False)
			new_item.created_by = request.user
			new_item.save()
			formItem = itemForm(request.user)
			alert = "Success !! Item has added."
	else:
		formItem = itemForm(request.user)

	return render_to_response('web_item_form.html',{		
		'formItem': formItem,
		'alert': alert,
	}, context_instance=RequestContext(request))

@login_required(login_url='/auth')
def ItemShowView(request, item_id):
	
	try:
		viewItem = item.objects.get(id=item_id, created_by=request.user)
	except item.DoesNotExist:
		return HttpResponseRedirect('/category/list/all/')
	
	return render_to_response('web_item_view.html',{			
		'item': viewItem,
	}, context_instance=RequestContext(request))

@login_required(login_url='/auth')
def ItemEditView(request, item_id):
	alert = None

	try:
		viewItem = item.objects.get(id=item_id, created_by=request.user)
	except item.DoesNotExist:
		return HttpResponseRedirect('/category/list/all/')

	if request.method == "POST":
		formItem = itemForm(request.user, request.POST)
		if formItem.is_valid():
			upd_item = formItem.save(commit=False)			
			upd_item.save()			
			alert = "Success !! Item has updated."
	else:
		formItem = itemForm(request.user, instance=viewItem)
	
	return render_to_response('web_item_form.html',{
		'formItem': formItem,
		'alert': alert,
	}, context_instance=RequestContext(request))


@login_required(login_url='/auth')
def ItemDeleteView(request, item_id):

	try:
		viewItem = item.objects.get(id=item_id, created_by=request.user)
		viewItem.delete()
	except item.DoesNotExist:
		return HttpResponseRedirect('/category/list/all/')

	if request.is_ajax():
		return HttpResponse(
			json.dumps({'status':200}), 
			mimetype="application/json"
		)

	else:
		return HttpResponseRedirect('/category/list/all/')

@login_required(login_url='/auth')
def CategoryNewView(request):		
	alert = None

	if request.method == "POST":
		formCategory = categoryForm(request.user, request.POST)
		if formCategory.is_valid():
			new_category = formCategory.save(commit=False)
			new_category.created_by = request.user
			new_category.save()
			formCategory = categoryForm(request.user)
			alert = "Success !! Category has added."
	else:
		formCategory = categoryForm(request.user)

	return render_to_response('web_category_form.html',{		
		'formCategory': formCategory,
		'alert': alert,
	}, context_instance=RequestContext(request))

@login_required(login_url='/auth')
def CategoryView(request, name_category):
	
	if name_category == "all":
		list_items = item.objects.filter(created_by=request.user)
	else:
		list_items = item.objects.filter(created_by=request.user, category__name=name_category)

	if "search" in request.GET and len(request.GET["search"]) > 0:
		list_items = list_items.filter(Q(name__contains=request.GET["search"]) | Q(username__contains=request.GET["search"]) | Q(password__contains=request.GET["search"]) | Q(url__contains=request.GET["search"]) | Q(comments__contains=request.GET["search"]))

	paginator = Paginator(list_items, nitems)

	page = request.GET.get('page')
    
	try:
		list_items = paginator.page(page)
	except PageNotAnInteger:
		list_items = paginator.page(1)
	except EmptyPage:        
		list_items = paginator.page(paginator.num_pages)

	return render_to_response('web_category.html',{						
			'list_items': list_items,
			'name_category': name_category,			
		}, context_instance=RequestContext(request))

@csrf_protect
def AuthView(request):
    if request.user.is_authenticated(): return HttpResponseRedirect('/')

    message = ""
    username = ""
    password = ""

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                try:
                    url_forward = request.GET["next"]
                except:
                    url_forward = '/category/list/all/'

                return HttpResponseRedirect(url_forward)
            else:
                message = "Tu cuenta no esta activa, por favor, contacta con el administrador."
        else:
            message = "Tu usuario y/o contraseña son incorrectos."
    
    return render_to_response(
        'web_login.html', {'message':message, 'username': username}, context_instance=RequestContext(request)
    )

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/')

def readpasswords():
	f = open('Passwords.csv', 'r')
	passwords = []

	for line in f.readlines():
		passwords.append(line.split(';'))

	for password in passwords[1:]:
		new_item = item()
		new_item.url = password[5]
		new_item.name = password[2]
		new_item.category_id = int(password[1])
		new_item.username = password[3]
		new_item.password = password[4]
		new_item.never_expire = True
		new_item.comments = password[6]
		new_item.created_by_id = 1
		new_item.save()



