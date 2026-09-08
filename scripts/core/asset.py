class OTAsset:

    def __init__(
        self,
        chassis_id=None,
        port_id=None,
        system_name=None,
        system_description=None,
        management_address=None,
        ttl=None
    ):

        self.chassis_id = chassis_id
        self.port_id = port_id
        self.system_name = system_name
        self.system_description = system_description
        self.management_address = management_address
        self.ttl = ttl

        self.observation_count = 0

    def record_observation(self):

        self.observation_count += 1

    def to_dict(self):

        return {
            "chassis_id": self.chassis_id,
            "port_id": self.port_id,
            "system_name": self.system_name,
            "system_description": self.system_description,
            "management_address": self.management_address,
            "ttl": self.ttl,
            "observation_count": self.observation_count
        }