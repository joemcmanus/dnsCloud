#!/usr/bin/env python3
# File    : sniff.py 
# Purpose : A program to sniff DNS requests and write to a file
# Author  : Joe McManus josephmc@alumni.cmu.edu
# Version : 0.1  05/14/2018 Joe McManus
# Copyright (C) 2018 Joe McManus
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with 


from scapy.all import *
import sys
import argparse

parser = argparse.ArgumentParser(description='DNS Sniffer')
parser.add_argument('interface', help="Network Interface", type=str)
parser.add_argument('outfile', help="DNS log file", type=str)
parser.add_argument('--pid', help="Create a pid file in /var/run/pysniff.pid",  action="store_true")

args=parser.parse_args()

if args.pid:
    fh=open("/var/run/pysniff.pid", "w")
    fh.write(str(os.getpid()))
    fh.close()

interface = args.interface

def querysniff(pkt):
    fh=open(args.outfile, "a")
    if IP in pkt:
        if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
            lookup=pkt.getlayer(DNS).qd.qname
            if "arpa" not in str(lookup):
                fh.write(str(lookup, 'utf-8') + "\n")

    fh.close()

sniff(iface = interface,filter = "port 53", prn = querysniff, store = 0)


