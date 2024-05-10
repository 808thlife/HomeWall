from django.urls import path

from . import views

app_name = "index"

urlpatterns = [
    path("", views.index_redirect, name = "index_redirect")
]
