from django.urls import path
from . import views

urlpatterns = [
    path("", views.detail, name="Home"),
    path("login/", views.loginView, name="Login"),



]