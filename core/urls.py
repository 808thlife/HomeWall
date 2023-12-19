from django.urls import path 
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name = "index"),
    path("rules/", views.rulesView, name = "rulesView"),
    path("users/", views.users, name = "users"),
    # path("sysinfo/ram", views.SysInfo.cpu_graph),
    # path("sysinfo/cpu", views.SysInfo.ram_graph),
    # path("sysinfo/storage", views.SysInfo.storage_graph),
]
