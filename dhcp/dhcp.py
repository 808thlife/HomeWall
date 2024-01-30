from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, UDP
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.sendrecv import sendp
from scapy.all import sniff

def dhcp_server(pkt):
    if DHCP in pkt and pkt[DHCP].options[0][1] == 3:  # DHCP Discover
        client_mac = pkt[Ether].src
        dhcp_offer = Ether(dst=client_mac, src='00:11:22:33:44:55') / \
                     IP(src='192.168.1.1', dst='255.255.255.255') / \
                     UDP(sport=67, dport=68) / \
                     BOOTP(op=2, yiaddr='192.168.1.100', siaddr='192.168.1.1', chaddr=client_mac) / \
                     DHCP(options=[('message-type', 'offer'),
                                   ('subnet_mask', '255.255.255.0'),
                                   ('router', '192.168.1.1'),
                                   ('domain', 'yourdomain.com'),
                                   'end'])
        sendp(dhcp_offer)
        print("DHCP Offer sent to client with MAC:", client_mac)

sniff(filter="udp and (port 67 or port 68)", prn=dhcp_server)
