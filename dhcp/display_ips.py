
from scapy.all import ARP, Ether, srp
import socket

def scan_network():
    # Define the IP range to scan
    target_ip = "192.168.1.0/24"  # Example subnet, adjust according to your network

    # Perform ARP scan
    arp_request = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC address
    arp_broadcast = ether / arp_request
    answered_list = srp(arp_broadcast, timeout=1, verbose=False)[0]

    # Gather device information
    devices = []
    for element in answered_list:
        device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices.append(device_info)

    # Resolve hostnames
    for device in devices:
        try:
            hostname = socket.gethostbyaddr(device["ip"])[0]
            print(hostname)
            device["hostname"] = hostname
        except socket.herror:
            device["hostname"] = "Unknown"

    return devices