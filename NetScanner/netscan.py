#!/usr/bin/env python

from numpy import broadcast
import scapy.all as scapy 
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_broadcast, verbose=False, timeout=1)[0]

    clients_list = []
    for el in answered_list:
        client_dict = {"ip": el[1].psrc, "mac": el[1].hwsrc }
        clients_list.append(client_dict)
    return clients_list
def print_result(results_list):

    print("IP\t\t\t\tMAC address\n" + "-"*60)

    for client in results_list:
        print(client['ip'] + "\t\t\t" + client['mac'])

options = get_args()
result = scan(options.target)
print_result(result)
                