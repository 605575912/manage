"""manage URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from manage.src.file import myserver
from manage.src.default import defalutserver
from manage.src.launcher import launcher
from manage.src.banners import banners  
from manage.src.login import login   
from manage.src.tabs import tabs 
from manage.src.userregister import userregister
from manage.src.mine import getmine      
from manage.src.image import getimage
from manage.src.music import getmusic  
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^server/$', myserver),
    url(r'^$', defalutserver),
    url(r'^launcher/$', launcher),
    url(r'^banner/$', banners),
    url(r'^tabs/$', tabs),
    url(r'^login/$', login),
    url(r'^register/$', userregister),
    url(r'^mine/$', getmine), 
    url(r'^img/.*?$', getimage),
    url(r'^music/.*?$', getmusic),
]
