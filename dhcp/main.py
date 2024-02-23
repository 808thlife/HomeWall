from dhcppython.dhcp import DhcpServer
from dhcppython.options import DHCPOption, MessageTypeOption
from dhcppython.utils import mac_to_bytes, ip_to_bytes

def dhcp_handler(pkt, addr):
    print("Received DHCP packet from:", addr)

    if pkt.options[MessageTypeOption].message_type == MessageTypeOption.DHCPDISCOVER:
        # Handle DHCP Discover packet
        print("DHCP Discover received")
        offer_pkt = pkt.reply()
        offer_pkt.add_option(DHCPOption('server_id', ip_to_bytes('127.0.0.1')))
        offer_pkt.add_option(DHCPOption('subnet_mask', ip_to_bytes('255.255.255.0')))
        offer_pkt.add_option(DHCPOption('router', ip_to_bytes('127.0.0.1')))
        offer_pkt.add_option(DHCPOption('lease_time', 3600))
        offer_pkt.add_option(DHCPOption('domain_name', b'example.com'))
        return offer_pkt

    elif pkt.options[MessageTypeOption].message_type == MessageTypeOption.DHCPREQUEST:
        # Handle DHCP Request packet
        print("DHCP Request received")
        ack_pkt = pkt.reply()
        ack_pkt.add_option(DHCPOption('server_id', ip_to_bytes('127.0.0.1')))
        ack_pkt.add_option(DHCPOption('subnet_mask', ip_to_bytes('255.255.255.0')))
        ack_pkt.add_option(DHCPOption('router', ip_to_bytes('127.0.0.1')))
        ack_pkt.add_option(DHCPOption('lease_time', 3600))
        ack_pkt.add_option(DHCPOption('domain_name', b'example.com'))
        return ack_pkt

if __name__ == "__main__":
    server = DhcpServer(interface='lo', port=8000, handler=dhcp_handler)
    server.start()
