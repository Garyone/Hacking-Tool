from scapy.all import *

# rdpcap comes from scapy and loads in our pcap file
p = rdpcap('/root/Documents/exo/ch21.pcap')

try:
  for i in range(500):
     if not p[i].haslayer(DNS):
         continue
     if DNSQR in p[i]:
         if DNSRR in p[i] and len(p[i][DNSRR].rdata)>0:
             print("S[%i]: %r" % (i,p[i][DNSRR].rdata))
         else:
             print("C[%i]: %r" % (i,p[i][DNSQR].qname))

except IndexError:
       print("")
