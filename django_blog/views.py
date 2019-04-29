import sys
from django.shortcuts import render, render_to_response,\
    HttpResponseRedirect
from datetime import datetime
from django_blog.models import  BlogPost, Account, \
    UserForm, UserLoginForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.exceptions import ObjectDoesNotExist



def archive(request):
    post = BlogPost(title='mocktitle', body='mockbody',
                    timestamp=datetime.now())

    return render_to_response('homepage.html', {'posts':[post]})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():

            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']

            user=Account(user_name=username, user_password=password,
                         user_email=email)
            user.save()

            return render_to_response('success.html',{'username':username},
                                      RequestContext(request))
    else:
        uf = UserForm()
        return render_to_response('register.html', {'uf':uf})

@csrf_exempt
def login(request):

    if request.method=='POST':
        print("post")
        uf = UserLoginForm(request.POST)
        if uf.is_valid():

            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']

            try:
                user = Account.objects.get(user_name=username,user_password=password)
                print("canget")
                return render_to_response('success.html',{'username':username},
                                         RequestContext(request))
            except ObjectDoesNotExist:
                return HttpResponseRedirect('/login/',{'uf':uf},
                                           RequestContext(request))
    else:
        print("login")
        uf = UserLoginForm()
    return render_to_response('login.html',{'uf':uf},
                              RequestContext(request))

