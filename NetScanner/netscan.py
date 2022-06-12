#!/usr/bin/env python

from numpy import broadcast
import scapy.all as scapy 

def scan(ip):
    arp_requst = scapy.ARP()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    print(broadcast.summary())

scan("10.0.2.1/24")