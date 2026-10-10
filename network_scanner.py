#!/usr/bin/env python
print("1. Starting script..")
import scapy.all as scapy
print("2. Scapy imported successfully")


def scan(ip):
    print("3. Inside scan function")
    arp_request = scapy.ARP(pdst=ip)
    print("4. ARP request created")
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    print("5. Ethernet broadcast created")
    arp_request_broadcast = broadcast/arp_request
    print("6.Combined packet created")

    print("7. Attempting to show packet")
    arp_request_broadcast.show()
    print("8. Packet shown successfully")


print("9. About to call scan")
scan("10.0.2.2/24")
print("10. Script finished")
