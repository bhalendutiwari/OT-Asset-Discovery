from scripts.core.asset import OTAsset
from scripts.core.inventory import AssetInventory


print("OTAsset Inventory Integration Test")
print("==================================")


inventory = AssetInventory()


asset = OTAsset(
    chassis_id="00:11:22:33:44:55",
    port_id="GigabitEthernet1/0/1",
    system_name="PLC-01",
    system_description="Siemens S7-1500 PLC",
    management_address="192.168.1.10",
    ttl=120
)


# Simulate the first packet observation.

asset.record_observation()


inventory.add_asset(asset)


# Simulate another observation of the
# same physical asset.

second_observation = OTAsset(
    chassis_id="00:11:22:33:44:55",
    port_id="GigabitEthernet1/0/1",
    system_name="PLC-01",
    system_description="Siemens S7-1500 PLC",
    management_address="192.168.1.10",
    ttl=120
)


second_observation.record_observation()


inventory.add_asset(
    second_observation
)


print("\nInventory")
print("=========")

inventory.show_assets()


print("\nValidation")
print("==========")

print(
    "Unique Assets :",
    inventory.total_assets()
)

print(
    "Observations  :",
    inventory.assets[0].observation_count
)


assert inventory.total_assets() == 1

assert (
    inventory.assets[0].observation_count == 2
)

assert (
    inventory.assets[0].system_name
    == "PLC-01"
)


print("\nOTAsset inventory test passed!")