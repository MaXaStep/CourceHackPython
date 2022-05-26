#!/bin/python3
import subprocess
import optparse


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


options = get_args()
change_mac(options.interface, options.new_mac)
