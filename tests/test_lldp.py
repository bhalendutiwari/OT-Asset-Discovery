from scapy.all import Ether, Raw

from scripts.lldp.lldp_parser import LLDPParser


print("LLDP Real Packet Test")
print("=====================")


# Create a synthetic LLDP Ethernet frame.
#
# EtherType 0x88CC = LLDP


# -------------------------------------------------
# Chassis ID TLV
# -------------------------------------------------
#
# Type   = 1
# Length = 7
#
# Value:
# Subtype = 4 (MAC Address)
# MAC     = 00:11:22:33:44:55
#
# TLV header = 0x0207

chassis_tlv = bytes.fromhex(
    "02 07"
    "04 00 11 22 33 44 55"
)


# -------------------------------------------------
# Port ID TLV
# -------------------------------------------------
#
# Type   = 2
# Length = 20
#
# Value:
# Subtype = 5 (Interface Name)
# Name    = GigabitEthernet1/0/1
#
# TLV header = 0x0414

port_tlv = bytes.fromhex(
    "04 15"
) + bytes([5]) + b"GigabitEthernet1/0/1"


# -------------------------------------------------
# TTL TLV
# -------------------------------------------------
#
# Type   = 3
# Length = 2
# Value  = 120 seconds
#
# TLV header = 0x0602

ttl_tlv = bytes.fromhex(
    "06 02"
    "00 78"
)


# -------------------------------------------------
# End of LLDPDU
# -------------------------------------------------
#
# Type   = 0
# Length = 0

end_tlv = bytes.fromhex(
    "00 00"
)


lldp_payload = (
    chassis_tlv
    + port_tlv
    + ttl_tlv
    + end_tlv
)


packet = Ether(
    src="00:11:22:33:44:55",
    dst="01:80:c2:00:00:0e",
    type=0x88CC
) / Raw(
    load=lldp_payload
)


parser = LLDPParser()


result = parser.parse(
    packet
)


print("\nParser Result")
print("=============")

for item in result:

    print(item)