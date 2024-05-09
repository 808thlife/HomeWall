from django.urls import path

from . import views

app_name = "filter"

urlpatterns = [
    path("add/", views.add_filter, name = "add_filter"),
    path("edit/<int:ID>", views.edit_filter, name = "edit_filter"),
    path("delete/<int:ID>", views.delete_filter, name = "delete_filter")
]
