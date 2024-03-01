from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from dhcp.utils import *
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

@staff_member_required(login_url=LOGIN_URL)
def user_profile(request, id):
    return render(request, "core/users-profile.html")

@staff_member_required(login_url=LOGIN_URL)
def dhcp_view(request):
    values = parse_config("./dhcp/dnsmasq.conf")
    print(values)

    address = values["address"]
    start_ip = values["start"]
    end_ip = values["end"]
    context = {"address": address, "start":start_ip, "end":end_ip}
    return render(request, "core/dhcp.html", context)
