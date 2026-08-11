from scapy.all import Ether, IP, ICMP, wrpcap

# Create two simple packets
pkt1 = Ether(
    src="00:11:22:33:44:55",
    dst="66:77:88:99:AA:BB"
) / IP(
    src="192.168.1.10",
    dst="192.168.1.20"
) / ICMP()

pkt2 = Ether(
    src="66:77:88:99:AA:BB",
    dst="00:11:22:33:44:55"
) / IP(
    src="192.168.1.20",
    dst="192.168.1.10"
) / ICMP()

# Save the packets into a PCAP file
wrpcap("pcaps/sample_lldp.pcap", [pkt1, pkt2])

print("Sample PCAP created successfully!")