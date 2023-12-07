from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from HomeWall.settings import LOGIN_URL
# Create your views here.

@staff_member_required(login_url=LOGIN_URL)
def index(request):
    return render(request, "core/index.html")

@staff_member_required(login_url=LOGIN_URL)
def rulesView(request):
    return render(request, "core/rules.html")

@staff_member_required(login_url=LOGIN_URL)
def users(request):
    return render(request, "core/users.html")