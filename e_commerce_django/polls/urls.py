from django.urls import path

from . import views

urlpatterns = [
    path("", views.index , name="index"),
    path("signin/",views.singnin,name="singin"),
    path("login/", views.login ,name = "login")
]