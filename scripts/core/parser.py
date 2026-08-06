from scapy.all import rdpcap
from scapy.layers.l2 import Ether


class PacketParser:

    def __init__(self, pcap_file):
        self.pcap_file = pcap_file

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

        self.detect_protocol(ethertype)

    def detect_protocol(self, ethertype):

        if ethertype == 0x0800:
            protocol = "IPv4"

        elif ethertype == 0x0806:
            protocol = "ARP"

        elif ethertype == 0x86DD:
            protocol = "IPv6"

        elif ethertype == 0x88CC:
            protocol = "LLDP"

        else:
            protocol = "Unknown"

        print("Protocol        :", protocol)