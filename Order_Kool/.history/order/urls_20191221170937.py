from django.urls import path
from . import views

urlpatterns = [
    path("", views.detail, name="Home"),
    path("", views.loginView, name="Login"),



]