
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Lister
from cloneapp.forms import UserForm, ListerForm
# Create your views here.


def view_index(request):
    return HttpResponse("YAY YOU MADE IT")


def view_create_user(request):
    if request.method == "GET":
        user_form = UserForm()
        lister_form = ListerForm()
    elif request.method == "POST":
        user_form = UserForm(request.POST)
        lister_form = ListerForm(request.POST)
        if user_form.is_valid() and lister_form.is_valid():
            user = user_form.save()
            rater = lister_form.save(commit=False)
            rater.user = user
            rater.save()
            login(request, user)
            password = user.password
            user.set_password(password)
            user.save()
            user = authenticate(username = user.username, password =password)
            login(request, user)
            return HttpResponseRedirect('/cloneapp/profile/')
    return render(request, 'create_user.html', {'user_form': user_form, 'lister_form': lister_form})


def view_profile(request):
    return render(request, 'profile.html')


def view_main(request):
    return render(request, 'main.html')
