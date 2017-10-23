from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reg$', views.reg),
    url(r'^login$', views.login),
    url(r'^regsuccess$', views.regsuccess),
    url(r'^loginsuccess$', views.loginsuccess),
]