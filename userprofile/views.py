from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from userprofile.models import UserLoginForm

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            user = authenticate(username = user_data["username"],
                                password = user_data["password"])
            # If successfully log in
            if user:
                login(request, user)
                return redirect("")
            else:
                return HttpResponse("Wrong username or password, please login again!")
        else:
            return HttpResponse("Invalid Input, please input again!")
    elif request.method == "GET":
        form = UserLoginForm()
        context = {"form":form}

        return render(request, 'homepage.html', context)




