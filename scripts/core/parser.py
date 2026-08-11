from scapy.all import rdpcap
from scapy.layers.l2 import Ether

from scripts.lldp.lldp_parser import LLDPParser


class PacketParser:

    def __init__(self, pcap_file):
        self.pcap_file = pcap_file
        self.lldp_parser = LLDPParser()

    def load_packets(self):

        print("\nLoading PCAP...")

        packets = rdpcap(self.pcap_file)

        print(f"Packets Loaded : {len(packets)}")

        print("\nPacket Summary")
        print("----------------")

        for packet in packets:

            print("\n==========================")

            self.display_packet(packet)

        return packets

    def display_packet(self, packet):

        print(packet.summary())

        self.show_ethernet_header(packet)

    def show_ethernet_header(self, packet):

        if Ether not in packet:
            return

        src_mac = packet[Ether].src
        dst_mac = packet[Ether].dst
        ethertype = packet[Ether].type

        print("Source MAC      :", src_mac)
        print("Destination MAC :", dst_mac)
        print("EtherType       :", hex(ethertype))

        self.detect_protocol(packet, ethertype)

    def detect_protocol(self, packet, ethertype):

        if ethertype == 0x0800:
            print("Protocol        : IPv4")

        elif ethertype == 0x0806:
            print("Protocol        : ARP")

        elif ethertype == 0x86DD:
            print("Protocol        : IPv6")

        elif ethertype == 0x88CC:
            print("Protocol        : LLDP")

            self.lldp_parser.parse(packet)

        else:
            print("Protocol        : Unknown")