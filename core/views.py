from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from dhcp.utils import *
from HomeWall.settings import LOGIN_URL
from accounts.models import User
from dhcp.display_ips import scan_network

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

    address = values["address"]
    start_ip = values["start_ip"]
    end_ip = values["end_ip"]
    mask = values["mask"]
    restart_time = values["restart_time"]

    #get ip table
    ips_arr = scan_network()

    context = {"address": address, "start":start_ip, 
    "end":end_ip, "dhcp_mask":mask, "restart_time": restart_time, "table":ips_arr}
    return render(request, "core/dhcp.html", context)
