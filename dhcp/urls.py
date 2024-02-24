from django.urls import path
from . import views

app_name = "dhcp"

urlpatterns = [
    path("", views.change_dhcp_form, name = "change_dhcp")
]
