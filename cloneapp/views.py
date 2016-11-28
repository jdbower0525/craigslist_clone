
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from cloneapp import models
from cloneapp.models import Lister, Item
from cloneapp.forms import UserForm, ListerForm, ItemForm
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
            lister = lister_form.save(commit=False)
            lister.user = user
            lister.save()
            login(request, user)
            password = user.password
            user.set_password(password)
            user.save()
            user = authenticate(username = user.username, password =password)
            login(request, user)
            return HttpResponseRedirect('/cloneapp/profile/')
    return render(request, 'create_user.html', {'user_form': user_form, 'lister_form': lister_form})


def view_add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.lister_id = request.user.id
            item.save()
            return HttpResponseRedirect('/cloneapp/profile')
    else:
        form = ItemForm()
        return render(request, "add_item.html", {'form': form})


def view_profile(request):
    all_items = models.Item.objects.all()
    return render(request, 'profile.html', {'all_items': all_items})


def view_main(request):
    return render(request, 'main.html')


def view_lister_detail(request, d):
    lister = models.Lister.objects.get(pk=d)
    all_items = lister.item_set.order_by("-price")
    return render(request, 'lister_detail.html',
                  {'lister': lister, 'all_items': all_items})
