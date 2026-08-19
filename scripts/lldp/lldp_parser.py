class LLDPParser:

    def __init__(self):
        print("LLDP Parser Initialized")

    def parse(self, packet):

        print("\nLLDP Packet Detected")

        asset = {
            "chassis_id": self.parse_chassis_id(packet),
            "port_id": self.parse_port_id(packet),
            "system_name": self.parse_system_name(packet),
            "system_description": self.parse_system_description(packet),
            "management_address": self.parse_management_address(packet)
        }

        return asset

    def parse_chassis_id(self, packet):
        return None

    def parse_port_id(self, packet):
        return None

    def parse_system_name(self, packet):
        return None

    def parse_system_description(self, packet):
        return None

    def parse_management_address(self, packet):
        return None