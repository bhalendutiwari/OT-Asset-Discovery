from scripts.lldp.tlv_decoder import LLDPDecoder


decoder = LLDPDecoder()


print("LLDP Port ID Decoder Test")
print("=========================")


# Port ID subtype:
# 5 = Interface Name

port_subtype = bytes([5])

port_name = b"GigabitEthernet1/0/1"

port_value = (
    port_subtype
    + port_name
)


result = decoder.decode_port_id(
    port_value
)


print("\nDecoded Port ID")
print("----------------")

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