import sys
from scapy.all import *

p = sr1(IPField(dst='192.168.1.1')/IPV6_ADDR_CAST_MASK)
if p: p.show()
