from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("home/", views.home, name="home"),
  path("login/", views.login, name="login"),
  path("Login", views.login, name="Login"),
  path("Login/", views.login, name="Login-slash"),
]
