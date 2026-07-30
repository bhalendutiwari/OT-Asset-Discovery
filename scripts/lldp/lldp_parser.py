import json

"""
LLDP Parser
Author: Bhalendu Tiwari

OT Asset Discovery Project
"""

def print_banner():
    print("=" * 50)
    print("      OT Asset Discovery - LLDP Parser")
    print("=" * 50)


def load_assets():
    with open("assets/demo_assets.json", "r") as file:
        assets = json.load(file)

    return assets

def display_asset(asset):
    print("\nDiscovered Asset\n")

    for key, value in asset.items():
        print(f"{key:<15}: {value}")

def display_summary(assets):
    print("\n====================================")
    print("OT Asset Inventory Summary")
    print("====================================")

    print(f"Total Assets : {len(assets)}")

    vendors = set()

    for asset in assets:
        vendors.add(asset["Vendor"])

    print(f"Unique Vendors : {len(vendors)}")
    print("Vendor List    :", ", ".join(vendors))


def main():
    print_banner()

    assets = load_assets()

    for index, asset in enumerate(assets, start=1):
        print(f"\n========== Asset {index} ==========")
        display_asset(asset)

    display_summary(assets)


if __name__ == "__main__":
    main()