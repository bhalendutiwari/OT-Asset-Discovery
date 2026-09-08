from scripts.core.inventory import AssetInventory


print("OT Asset Deduplication Test")
print("===========================")


inventory = AssetInventory()


plc_asset = {
    "chassis_id": "00:11:22:33:44:55",
    "port_id": "GigabitEthernet1/0/1",
    "system_name": "PLC-01",
    "system_description": "Siemens S7-1500 PLC",
    "management_address": "192.168.1.10",
    "ttl": 120
}


# Simulate the same PLC being
# observed five times.

for _ in range(5):

    inventory.add_asset(
        plc_asset.copy()
    )


print("\nInventory Result")
print("================")

inventory.show_assets()


print("\nValidation")
print("==========")

print(
    "Unique Assets :",
    inventory.total_assets()
)

print(
    "Observations  :",
    inventory.assets[0]["observation_count"]
)


assert inventory.total_assets() == 1

assert (
    inventory.assets[0]["observation_count"] == 5
)


print("\nDeduplication test passed!")