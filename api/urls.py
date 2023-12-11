from django.urls import path 
from . import views

app_name = "api"

urlpatterns = [
    path("", views.UserModelView.as_view(), name = "index"),
    path("<int:id>", views.UserModelView.as_view(), name = "delete")
]
