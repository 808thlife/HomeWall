import socket
import threading
import time
from django.core.management.base import BaseCommand
from accounts.models import User

IP_ADDRESS_PREFIX = '192.168.1.'
STARTING_IP = 100
MAX_DEVICES = 50
LEASE_DURATION = 60  # Lease duration in seconds (1 minute)

leased_ips = {}
available_ips = set()  # Track available IP addresses separately

lock = threading.Lock()

class Command(BaseCommand):
    help = 'Starts a DHCP-like server'

    def handle(self, *args, **options):
        lease_expiry_thread = threading.Thread(target=self.lease_expiry_check, daemon=True)
        lease_expiry_thread.start()

        # Initialize available_ips with all possible IP addresses
        for i in range(STARTING_IP, STARTING_IP + MAX_DEVICES):
            available_ips.add(IP_ADDRESS_PREFIX + str(i))

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 8888))
        server_socket.listen(5)
        self.stdout.write(self.style.SUCCESS("DHCP-like server is running on port 8888..."))

        while True:
            client_socket, client_address = server_socket.accept()
            self.stdout.write(self.style.SUCCESS(f"Connection from {client_address}"))

            ip_address = self.assign_ip_address()
            print(ip_address)
            client_socket.send(ip_address.encode())
            

    def assign_ip_address(self):
        global leased_ips

        # Use a previously leased IP if available
        with lock:
            if available_ips:
                ip_address = available_ips.pop()
                leased_ips[ip_address] = time.time() + LEASE_DURATION
                return ip_address

        # Otherwise, assign the next available IP
        global STARTING_IP
        ip_address = IP_ADDRESS_PREFIX + str(STARTING_IP)
        STARTING_IP += 1
        leased_ips[ip_address] = time.time() + LEASE_DURATION
        return ip_address

    def lease_expiry_check(self):
        global leased_ips

        while True:
            time.sleep(1)

            current_time = time.time()
            expired_ips = [ip for ip, expiry_time in leased_ips.items() if expiry_time <= current_time]
            for ip in expired_ips:
                del leased_ips[ip]
                available_ips.add(ip)
                self.stdout.write(self.style.SUCCESS(f"Lease expired for IP address {ip}"))
