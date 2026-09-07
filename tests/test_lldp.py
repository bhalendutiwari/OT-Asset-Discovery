from scapy.all import Ether, Raw

from scripts.lldp.lldp_parser import LLDPParser


print("LLDP Complete Asset Test")
print("========================")


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
# System Name TLV
# -------------------------------------------------
#
# Type   = 5
# Length = 6
# Value  = PLC-01
#
# Header = 0x0A06

system_name_tlv = bytes.fromhex(
    "0A 06"
) + b"PLC-01"


# -------------------------------------------------
# System Description TLV
# -------------------------------------------------
#
# Type   = 6
# Length = 19
# Value  = Siemens S7-1500 PLC
#
# Header = 0x0C13

system_description_tlv = bytes.fromhex(
    "0C 13"
) + b"Siemens S7-1500 PLC"


# -------------------------------------------------
# Management Address TLV
# -------------------------------------------------
#
# Type   = 8
#
# Address String Length = 5
# Address Subtype       = 1 (IPv4)
# Address               = 192.168.1.10
#
# Header = 0x1005

management_tlv = bytes.fromhex(
    "10 06"
    "05"
    "01"
    "C0 A8 01 0A"
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
    + system_name_tlv
    + system_description_tlv
    + management_tlv
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