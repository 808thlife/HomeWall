from django.urls import path 
from . import views

app_name = "api"

urlpatterns = [
    path("", views.UserModelView.as_view(), name = "index"),
    path("<int:id>", views.UserModelView.as_view(), name = "delete"),
    path("sysinfo/ram", views.get_ram_usage),
    path("sysinfo/cpu", views.get_cpu_usage)
]
