# helloworld/urls.py
from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('<str:username>', views.count)
]
