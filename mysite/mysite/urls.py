"""mysite URL Configuration

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
from django.http import HttpResponse
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name="test.html")),
    url(r'^$', views.home, name='home'),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^hextime/', include('hextime.urls')),
    url(r'^bintime/', include('bintime.urls')),
    url(r'^itemstore/', include('itemstore.urls')),
    url(r'^googlee7941072fd1ee0cb\.html$', lambda r: HttpResponse("google-site-verification: googlee7941072fd1ee0cb.html")),
]
