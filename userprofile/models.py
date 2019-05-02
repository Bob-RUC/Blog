from django.db import models
import django.forms as forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField()


