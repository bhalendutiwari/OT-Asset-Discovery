from scripts.lldp.tlv_decoder import LLDPDecoder


decoder = LLDPDecoder()

print("LLDP Chassis ID Decoder Test")
print("============================")


# Chassis ID subtype:
# 4 = MAC Address

chassis_subtype = bytes([4])

chassis_mac = bytes.fromhex(
    "00 11 22 33 44 55"
)

chassis_value = (
    chassis_subtype
    + chassis_mac
)


result = decoder.decode_chassis_id(
    chassis_value
)


print("\nDecoded Chassis ID")
print("------------------")

print(
    "Subtype      :",
    result["subtype"]
)

print(
    "Subtype Name :",
    result["subtype_name"]
)

print(
    "Identifier   :",
    result["identifier"]
)