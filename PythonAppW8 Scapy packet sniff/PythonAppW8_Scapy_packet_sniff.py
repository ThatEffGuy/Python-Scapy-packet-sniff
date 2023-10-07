from scapy.all import *
num_to_sniff = 0
#asks how many packets want to be sniffed
num_to_sniff = int(input("enter the number of packets to sniff: "))
#sniff for selected packets
a=sniff(count=num_to_sniff) 
#print out the summary of packets
a.nsummary()