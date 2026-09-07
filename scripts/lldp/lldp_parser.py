from scripts.lldp.tlv_decoder import LLDPDecoder


class LLDPParser:

    def __init__(self):
        print("LLDP Parser Initialized")
        self.decoder = LLDPDecoder()

    def parse(self, packet):

        print("\nLLDP Packet Detected")

        # For Lesson 12 we use synthetic LLDP data.
        # Real packet extraction will be added later.

        chassis_value = (
            bytes([4])
            + bytes.fromhex("00 11 22 33 44 55")
        )

        port_value = (
            bytes([5])
            + b"GigabitEthernet1/0/1"
        )

        chassis_id = self.decoder.decode_chassis_id(
            chassis_value
        )

        port_id = self.decoder.decode_port_id(
            port_value
        )

        asset = {
            "chassis_id": chassis_id["identifier"],
            "port_id": port_id["identifier"],
            "system_name": None,
            "system_description": None,
            "management_address": None
        }

        return asset