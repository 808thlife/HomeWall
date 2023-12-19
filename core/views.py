from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from HomeWall.settings import LOGIN_URL
from accounts.models import User



@staff_member_required(login_url=LOGIN_URL)
def index(request):
    return render(request, "core/index.html")

@staff_member_required(login_url=LOGIN_URL)
def rulesView(request):
    return render(request, "core/rules.html")

@staff_member_required(login_url=LOGIN_URL)
def users(request):
    users = User.objects.all()
    context = {"users":users}
    return render(request, "core/users.html", context)

