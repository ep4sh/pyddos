from scapy.all import *

send(IP(dst="10.50.0.1")/fuzz(UDP()),loop=1)

