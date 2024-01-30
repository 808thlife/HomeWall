from django.urls import path
from . import views

urlpatterns = [
    path("", views.ip_address_list, name = "dhcp")
]
