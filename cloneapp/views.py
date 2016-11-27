
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from cloneapp.forms import UserForm
# Create your views here.


def view_index(request):
    return HttpResponse("YAY YOU MADE IT")


def view_create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            login(request, user)
            return HttpResponseRedirect('/cloneapp/')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})


def view_profile(request):
    return render(request, 'profile.html')


def view_main(request):
    return render(request, 'main.html')
