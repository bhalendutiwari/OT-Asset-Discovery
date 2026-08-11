from scripts.core.inventory import AssetInventory

inventory = AssetInventory()

inventory.add_asset({
    "Vendor": "Siemens",
    "Model": "S7-1200",
    "IP": "192.168.1.10"
})

inventory.add_asset({
    "Vendor": "WAGO",
    "Model": "750-8212",
    "IP": "192.168.1.20"
})

inventory.show_assets()