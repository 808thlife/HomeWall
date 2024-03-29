# from scapy.all import ARP, Ether, srp
# import socket

# # Function to perform ARP scan and gather device information
# def arp_scan(target_ip):
#     arp_request = ARP(pdst=target_ip)
#     ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC address

#     arp_broadcast = ether/arp_request

#     answered_list = srp(arp_broadcast, timeout=1, verbose=False)[0]

#     devices = []
#     for element in answered_list:
#         device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
#         devices.append(device_info)

#     return devices

# # Function to resolve hostname from IP address
# def resolve_hostname(ip):
#     try:
#         hostname, _, _ = socket.gethostbyaddr(ip)
#         return hostname
#     except socket.herror:
#         return None

# # Main function
# def get_ips():
#     target_ip = "192.168.1.0/24"  # Example subnet, adjust according to your network
#     ip_list = []
#     devices = arp_scan(target_ip)

#     for device in devices:
#         device["hostname"] = resolve_hostname(device["ip"])
#         ip_list.append(device)
#         #print(device)
#     return ip_list

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
            hostname, _, _ = socket.gethostbyaddr(device["ip"])
            device["hostname"] = hostname
        except socket.herror:
            device["hostname"] = "Unknown"

    return devices