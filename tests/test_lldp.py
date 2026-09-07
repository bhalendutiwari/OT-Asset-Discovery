from scapy.all import Ether, Raw

from scripts.lldp.lldp_parser import LLDPParser


print("LLDP Real Packet Test")
print("=====================")


# -------------------------------------------------
# Chassis ID TLV
# -------------------------------------------------

chassis_tlv = bytes.fromhex(
    "02 07"
    "04 00 11 22 33 44 55"
)


# -------------------------------------------------
# Port ID TLV
# -------------------------------------------------

port_tlv = bytes.fromhex(
    "04 15"
) + bytes([5]) + b"GigabitEthernet1/0/1"


# -------------------------------------------------
# TTL TLV
# -------------------------------------------------

ttl_tlv = bytes.fromhex(
    "06 02"
    "00 78"
)


# -------------------------------------------------
# End of LLDPDU
# -------------------------------------------------

end_tlv = bytes.fromhex(
    "00 00"
)


# Build complete LLDP payload

lldp_payload = (
    chassis_tlv
    + port_tlv
    + ttl_tlv
    + end_tlv
)


# Build Ethernet frame

packet = Ether(
    src="00:11:22:33:44:55",
    dst="01:80:c2:00:00:0e",
    type=0x88CC
) / Raw(
    load=lldp_payload
)


# Create parser

parser = LLDPParser()


# Parse packet

result = parser.parse(
    packet
)


# Display discovered asset

print("\nDiscovered Asset")
print("================")

for key, value in result.items():

    print(
        f"{key:<25}: {value}"
    )