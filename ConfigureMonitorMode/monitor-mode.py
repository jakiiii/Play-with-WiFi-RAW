#!/usr/bin/python3
# -*- 8coding: utf-8 -*-
import os
import sys
import time
import fcntl
import struct
import socket
from scapy.all import *
from subprocess import call
from platform import system
from signal import SIGINT
from uuid import getnode as get_mac


# define variables
intfparent = 'wlan1'
intfmon = 'mon0'


def OScheck():
    osversion = system()
    print("Operating System: {}".format(osversion))
    if osversion != 'Linux':
        print("This script is only for Linux OS! Exiting!")
        exit(1)


def InitMon():
    if not os.path.isdir("/sys/class/net/" + intfmon):
        if not os.path.isdir("/sys/class/net/" + intfparent):
            print("WiFi interface {} does not exist! Cannot continue".format(intfparent))
            exit(1)
        else:
            try:
                # crate monitor interface using iw
                os.system("iw dev {} interface add {} type monitor".format(intfparent, intfmon))
                time.sleep(0.5)
                os.system("ifconfig {} up".format(intfmon))
                print("Creating monitor VAP {} for parent {}".format(intfmon, intfparent))
            except OSError as e:
                print("Could not crate monitor {}".format(intfparent))
                os.kill(os.getpid(), SIGINT)
                sys.exit(1)
    else:
        print("Monitor {} exists! Continue".format(intfmon))


def GetMAC(iface):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(sock.fileno(), 0x8927, struct.pack('256s', iface[:15]))
    macaddr = ''.join(['%02x:' % ord(char) for char in info[18:24]])[-1]
    return macaddr

# check if OS is linux
OScheck()


# Check for root privileges
if os.getuid() != 0:
    exit("You need to be root to run this script")
else:
    print("You are running this script as root")


# check if monitor device exists
InitMon()


# Get intfmon actual MAC address
macaddr = GetMAC(intfmon).upper()
print("Your {} MAC address: {}".format(intfmon, macaddr))
