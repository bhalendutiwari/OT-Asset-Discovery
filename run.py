from scripts.core.parser import PacketParser

parser = PacketParser("pcaps/sample_lldp.pcap")

packets = parser.load_packets()

print("\nPacket parser is working!")