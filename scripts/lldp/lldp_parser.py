from scripts.lldp.tlv_decoder import LLDPDecoder


class LLDPParser:

    def __init__(self):
        print("LLDP Parser Initialized")
        self.decoder = LLDPDecoder()

    def parse(self, packet):

        print("\nLLDP Packet Detected")

        if packet is None:
            return self.parse_synthetic_data()

        return self.parse_packet(packet)

    def parse_packet(self, packet):

        # LLDP EtherType = 0x88CC

        raw_payload = bytes(packet.payload)

        print(
            "LLDP Payload Length :",
            len(raw_payload)
        )

        tlvs = self.decoder.decode_all(
            raw_payload
        )

        print("\nLLDP TLVs")
        print("---------")

        for tlv in tlvs:

            print(
                f"Type {tlv['type']}: "
                f"{tlv['name']} "
                f"(Length {tlv['length']})"
            )

        return tlvs

    def parse_synthetic_data(self):

        # Synthetic LLDP data for development.
        # Real packet extraction is handled by parse_packet().

        chassis_value = (
            bytes([4])
            + bytes.fromhex("00 11 22 33 44 55")
        )

        port_value = (
            bytes([5])
            + b"GigabitEthernet1/0/1"
        )

        ttl_value = bytes.fromhex("00 78")

        system_name_value = b"PLC-01"

        system_description_value = (
            b"Siemens S7-1500 PLC"
        )

        management_value = (
            bytes([5])
            + bytes([1])
            + bytes([192, 168, 1, 10])
        )

        chassis_id = self.decoder.decode_chassis_id(
            chassis_value
        )

        port_id = self.decoder.decode_port_id(
            port_value
        )

        ttl = self.decoder.decode_ttl(
            ttl_value
        )

        system_name = self.decoder.decode_system_name(
            system_name_value
        )

        system_description = (
            self.decoder.decode_system_description(
                system_description_value
            )
        )

        management_address = (
            self.decoder.decode_management_address(
                management_value
            )
        )

        asset = {
            "chassis_id": chassis_id["identifier"],
            "port_id": port_id["identifier"],
            "system_name": system_name,
            "system_description": system_description,
            "management_address": management_address["address"],
            "ttl": ttl
        }

        return asset