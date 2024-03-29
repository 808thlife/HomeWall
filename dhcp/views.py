import json

from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from HomeWall.settings import LOGIN_URL

from .display_ips import scan_network
from .utils import edit_dnsmasq_conf


@staff_member_required(login_url=LOGIN_URL)
def change_dhcp_form(request):
    if request.method == "POST":
        start_value = request.POST["dhcp-start"] # 1 It can't start with 0 because it was already taken by the address field in conf file
        ending_value = request.POST["dhcp-end"] #254
        address = request.POST["dhcp-address"] #  192.168.1 for instance
        mask = request.POST["dhcp-mask"]
        reset_time =  request.POST["dhcp-reset-time"]
        try:
            edit_dnsmasq_conf(f"{start_value}, {ending_value},{mask},{reset_time}", f"{address}", "./dhcp/dnsmasq.conf" )
        except FileNotFoundError:
            print("file was not found")
    return HttpResponseRedirect(reverse("core:dhcp_view"))

@staff_member_required(login_url=LOGIN_URL)
def get_dhcp_table(request):
    if request.method == "GET":
        table = scan_network()
        return JsonResponse(table, safe = False)
    return JsonResponse({"error":"POST/DELETE/PUT methods are not allowed."})