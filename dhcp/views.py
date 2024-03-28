from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .utils import edit_dnsmasq_conf

def change_dhcp_form(request):
    if request.method == "POST":
        start_value = request.POST["dhcp-start"] # 1 It can't start with 0 because it was already taken by the address field in conf file
        ending_value = request.POST["dhcp-end"] #254
        address = request.POST["dhcp-address"] #  192.168.1 for instance
        mask = request.POST["dhcp-mask"]
        reset_time =  request.POST["dhcp-reset-time"]
        try:
            edit_dnsmasq_conf(f"{start_value},{ending_value},{mask},{reset_time}", f"{address}", "./dhcp/dnsmasq.conf" )
        except FileNotFoundError:
            print("file was not found")
    return HttpResponseRedirect(reverse("core:dhcp_view"))