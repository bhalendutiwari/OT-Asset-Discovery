class LLDPParser:

    def __init__(self):
        print("LLDP Parser Initialized")

    def parse(self, packet):

        print("\nLLDP Packet Detected")

        self.parse_chassis_id()
        self.parse_port_id()
        self.parse_system_name()
        self.parse_management_address()

    def parse_chassis_id(self):
        print("Parsing Chassis ID...")

    def parse_port_id(self):
        print("Parsing Port ID...")

    def parse_system_name(self):
        print("Parsing System Name...")

    def parse_management_address(self):
        print("Parsing Management Address...")