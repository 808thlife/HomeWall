from django.urls import path 
from . import views

app_name = "api"

urlpatterns = [
    path("", views.get_users, name = "index"),
    path("add-user/", views.add_user, name = "add_user")
]
