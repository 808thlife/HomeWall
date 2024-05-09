from django.urls import path
from . import views

app_name = "iptables"

urlpatterns = [
    path("", views.index, name = "index"),
    path("create", views.create, name = "create"),
    path("delete/<int:ID>", views.delete, name = "delete"),
    path("edit/<int:ID>", views.edit, name = "edit")
]
