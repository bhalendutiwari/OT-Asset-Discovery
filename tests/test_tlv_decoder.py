from scripts.lldp.tlv_decoder import LLDPDecoder


decoder = LLDPDecoder()

print("Complete LLDPDU Decoder Test")
print("============================")


def create_tlv(tlv_type, value):

    tlv_length = len(value)

    header = (tlv_type << 9) | tlv_length

    return header.to_bytes(2, byteorder="big") + value


chassis_id = create_tlv(
    1,
    b"00:11:22:33:44:55"
)

port_id = create_tlv(
    2,
    b"Port-1"
)

ttl = create_tlv(
    3,
    (120).to_bytes(2, byteorder="big")
)

system_name = create_tlv(
    5,
    b"PLC-01"
)

system_description = create_tlv(
    6,
    b"Industrial PLC"
)

end_of_lldpdu = create_tlv(
    0,
    b""
)


lldp_data = (
    chassis_id
    + port_id
    + ttl
    + system_name
    + system_description
    + end_of_lldpdu
)


tlvs = decoder.decode_all(lldp_data)


print("\nDecoded TLVs")
print("============")

for tlv in tlvs:

    print(
        f"Type   : {tlv['type']}\n"
        f"Name   : {tlv['name']}\n"
        f"Length : {tlv['length']}\n"
        f"Value  : {tlv['value']}\n"
    )