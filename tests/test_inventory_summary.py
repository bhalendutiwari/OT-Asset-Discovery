from scripts.core.inventory import AssetInventory
import json

inventory = AssetInventory()

with open("assets/demo_assets.json", "r") as file:
    assets = json.load(file)

for asset in assets:
    inventory.add_asset(asset)

inventory.show_summary()