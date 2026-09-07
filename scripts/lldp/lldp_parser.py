from scripts.lldp.tlv_decoder import LLDPDecoder


class LLDPParser:

    def __init__(self):
        print("LLDP Parser Initialized")
        self.decoder = LLDPDecoder()

    def parse(self, packet):

        print("\nLLDP Packet Detected")

        # Synthetic LLDP data for development.
        # Real packet extraction will be added later.

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

        # Management Address:
        #
        # Address String Length = 5
        # Address Subtype       = 1 (IPv4)
        # Address               = 192.168.1.10
        #
        # The remaining fields are not yet decoded.

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