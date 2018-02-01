from django.contrib import admin

from django.conf.urls import include, url
from . import views

urlpatterns = [
	#path('', views.index, name='index'),
	url(r'^$', views.index, name='index'),
]