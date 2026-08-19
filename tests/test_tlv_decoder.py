from scripts.lldp.tlv_decoder import LLDPDecoder


decoder = LLDPDecoder()

print("LLDP TLV Binary Decoder Test")
print("============================")


# Create a System Name TLV
# Type = 5
# Value = "PLC-01"

tlv_type = 5
value = b"PLC-01"

tlv_length = len(value)

header = (tlv_type << 9) | tlv_length

tlv_data = header.to_bytes(2, byteorder="big") + value


result = decoder.decode(tlv_data)


print("Raw Data :", tlv_data)
print("Type     :", result["type"])
print("Name     :", result["name"])
print("Length   :", result["length"])
print("Value    :", result["value"].decode())