from django.shortcuts import render
from .utils import edit_dnsmasq_conf

def change_dhcp_form(request):
    if request.method == "POST":
        start_value = request.POST["dhcp-start"] # 1 It can't start with 0 because it was already taken by the address
        ending_value = request.POST["dhcp-end"] #254
        address = request.POST["dhcp-address"] #  192.168.1.0 for instance
        try:
            edit_dnsmasq_conf(f"{address}.{start_value}, {address}.{ending_value}", f"{address}.0", "./dhcp/dnsmasq.conf" )
        except FileNotFoundError:
            print("file was not found")
    return render(request, "core/dhcp.html")
