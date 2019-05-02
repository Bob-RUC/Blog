import sys
from django.shortcuts import render, render_to_response,\
    HttpResponseRedirect, HttpResponse
from datetime import datetime
from django_blog.models import  BlogPost, Account, \
    UserForm, UserLoginForm, PostBlogForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.exceptions import ObjectDoesNotExist



def archive(request):

    return render_to_response('homepage.html', {'posts':BlogPost.objects.all()})

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


def write_post(request):
    if request.method == 'POST':
        write_post = PostBlogForm(request.POST)
        if write_post.is_valid():
            title = write_post.cleaned_data('title')
            contents = write_post.cleaned_data('contents')


def home(request, my_args):
    return HttpResponse("You're looking at my_args %s" % my_args)

@csrf_exempt
def write(request):
    if request.method == 'GET':
        return render_to_response('write_blog.html')

    elif request.method == 'POST':
        title = request.POST.get('blog_title')
        body = request.POST.get('blog_body')
        time = datetime.now()

        new_post = BlogPost(title=title, body=body,
                            timestamp=time)
        print("new post")
        new_post.save()
        print("save")

        return HttpResponseRedirect('/blog/')
    else:
        return HttpResponse("fuck you!")
