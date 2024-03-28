import ping3

def ping_ip_addresses(ip_addresses):
    for ip in ip_addresses:
        try:
            # Perform ICMP ping to the IP address
            response = ping3.ping(ip)
            if response is not None:
                print(f"IP {ip} is online - Round-trip time: {response} ms")
            else:
                print(f"IP {ip} is offline")
        except Exception as e:
            print(f"Error while pinging {ip}: {e}")

# List of IP addresses from your DHCP table
dhcp_ip_addresses = [
    "192.168.1.2",
    "192.168.1.4",
    "192.168.1.5",
    "192.168.1.6"
]

ping_ip_addresses(dhcp_ip_addresses)
