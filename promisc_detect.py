from scapy.all import *
import ipaddress

# CHOOSE INTERFACE TO USE
for i in get_if_list():
 print(i)
iface=input("Type interface you wnat to use: ")

# GET MAC FROM IFACE
sender_mac=get_if_hwaddr(iface)

# DEFINE HOST OR NETWORK (e.g. 10.10.10.1 or 10.10.10.0/8)
scan_set=input("Type host address or subnet address to scan: ")
if "/" not in scan_set:
 scan_set=scan_set+"/32"
hosts=[str(i) for i in ipaddress.IPv4Network(scan_set)]

# PROMISC INTERFACES TEST
dst_eth=["FF:FF:FF:FF:FF:FE", "FF:FF:00:00:00:00", "FF:00:00:00:00:00"]
for z in hosts:
 error=0
 for i in dst_eth:
  ether=Ether()
  ether.dst=i
  arp=ARP()
  arp.hwsrc= sender_mac
  arp.pdst = z
  arp.dst = "i"
  arp.op = 1
  pkt=(ether/arp)
  response=srp1(pkt, iface=iface2, timeout=2, verbose=0)
  try:
    if response is None:
     raise ("Exception")
  except:
   error+=1
 if error >=1:
  print(z+": Non promiscuous mode detected !")
 else:
  print(z+": Promiscuous mode detected !")
