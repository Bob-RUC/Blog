from django.db import models
from django import forms

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()


class Account(models.Model):
    user_name = models.CharField(max_length=15)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=40)
    user_ticket = models.CharField(max_length=30, null=True)

class UserForm(forms.Form):
    username = forms.CharField(label='User Name：', max_length=100)
    password = forms.CharField(label='Password：', widget=forms.PasswordInput())
    email = forms.EmailField(label='Email：')

# 登录
#定义表单类型
class UserLoginForm(forms.Form):
    username=forms.CharField(label='User Name',max_length=100)
    password=forms.CharField(label='Password',widget=forms.PasswordInput())


class PostBlogForm(forms.Form):
    title = forms.CharField(max_length=150)
    contents = forms.Textarea()