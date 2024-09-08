from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from register import views as v

urlpatterns = [
    path("<int:id>", views.index, name="views"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("settings/", views.settings, name="settings"),
    path("", v.register, name="register")
]
