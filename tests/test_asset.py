from scripts.core.asset import OTAsset


print("OT Asset Model Test")
print("===================")


asset = OTAsset(
    chassis_id="00:11:22:33:44:55",
    port_id="GigabitEthernet1/0/1",
    system_name="PLC-01",
    system_description="Siemens S7-1500 PLC",
    management_address="192.168.1.10",
    ttl=120
)


print("\nInitial Asset")
print("-------------")

print(
    asset.to_dict()
)


# Record observations.

asset.record_observation()
asset.record_observation()
asset.record_observation()


# Record discovery evidence.

asset.add_evidence(
    "LLDP System Name",
    "PLC-01"
)

asset.add_evidence(
    "LLDP System Description",
    "Siemens S7-1500 PLC"
)

asset.add_evidence(
    "LLDP Management Address",
    "192.168.1.10"
)


print("\nAfter Observations and Evidence")
print("--------------------------------")

print(
    asset.to_dict()
)


assert asset.chassis_id == (
    "00:11:22:33:44:55"
)

assert asset.system_name == "PLC-01"

assert asset.management_address == (
    "192.168.1.10"
)

assert asset.observation_count == 3

assert len(asset.evidence) == 3

assert asset.evidence[0]["source"] == (
    "LLDP System Name"
)

assert asset.evidence[0]["value"] == (
    "PLC-01"
)


print("\nAsset model test passed!")