#!/bin/python3
import subprocess
import optparse
import re


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address for interface")
    (options, arguments) =  parser.parse_args()
    if not options.interface:
        print("[-] Error: Need argument interface")
        exit
    if not options.new_mac:
        print("[-] Error: Need argument new_mac")
        exit
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC of " + interface + " to " + new_mac )

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    output = subprocess.check_output(["ifconfig",interface])
    mac_addr = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output.decode('utf-8'))

    if mac_addr:
        return mac_addr.group(0)
    else:
        print("[-] Network adapter has no MAC address")


options = get_args()

current_mac = get_current_mac(options.interface)
print("Current mac: " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)  
if current_mac == options.new_mac: 
    print("[+] MAC address was succefully changed to " + current_mac)
else:
    print("[-] MAC has not been changed.")