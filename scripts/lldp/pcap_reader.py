from scapy.all import rdpcap
import os


PCAP_FILE = "pcaps/sample.pcapng"


def main():
    print("=" * 50)
    print("OT Asset Discovery - PCAP Reader")
    print("=" * 50)

    if not os.path.exists(PCAP_FILE):
        print(f"\nError: '{PCAP_FILE}' not found.")
        print("Please place a PCAP or PCAPNG file inside the 'pcaps' folder.")
        return

    try:
        packets = rdpcap(PCAP_FILE)
        print(f"\nSuccessfully loaded {len(packets)} packets.\n")

        for index, packet in enumerate(packets, start=1):
            print(f"Packet {index}")
            print(packet.summary())
            print("-" * 50)

    except Exception as error:
        print(f"Failed to read PCAP: {error}")


if __name__ == "__main__":
    main()