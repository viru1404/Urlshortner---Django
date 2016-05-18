from django.conf.urls import url, include
from django.contrib import admin
from .views import (
	short_home,
	visit_link,
	)

urlpatterns = [
   
    url(r'^$', short_home),
    url(r'^(?P<link>[\w.@*-]+)/$', visit_link),
    #url(r'^(?P<link>[\w.@*-]+)/$', short_home),
    #url(r'^store/$', store_link),
    #url(r'^store/(?P<idd>[\w.@*-]+)/$', store_link),
]