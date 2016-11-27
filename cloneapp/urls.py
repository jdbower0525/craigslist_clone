"""craigslist_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from cloneapp import views
import cloneapp
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.view_index, name='index'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/cloneapp/login/'},
        name='logout'),
    url(r'^create_user/$', views.view_create_user, name='create_user'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^main/$', views.view_main, name='main'),
    url(r'^profile/$', views.view_profile, name='profile'),
    url(r'^add_item/$', views.view_add_item, name='add_item'),
]
