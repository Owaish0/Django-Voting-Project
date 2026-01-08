from django.contrib import admin
from django.urls import path, include
from . import views
from django.shortcuts import redirect

urlpatterns = [
    # path("", lambda request: redirect("polls/")),
    path("", views.home, name = "home"),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
