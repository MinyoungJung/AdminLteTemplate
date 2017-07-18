"""cure_children URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from cure_children.views import HomeView, UserCreateView
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),   # Todo: 나중에 disable

    url(r'^', include('django.contrib.auth.urls')),
    url(r'register/$', UserCreateView.as_view(), name='register'),

    url(r'^login/$', auth_views.login, {'template_name': 'home.html'}),
]
