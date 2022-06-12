#!/usr/bin/env python

from numpy import broadcast
import scapy.all as scapy 

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_broadcast, verbose=False, timeout=1)[0]
    print("IP\t\t\t\tMAC address\n" + "-"*60)
    for el in answered_list:
        print(el[1].psrc + "\t\t\t" +el[1].hwsrc)
        print("-"*60)

scan("10.0.2.1/24")
