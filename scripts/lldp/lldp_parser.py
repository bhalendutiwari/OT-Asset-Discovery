"""
LLDP Parser
Author: Bhalendu Tiwari

OT Asset Discovery Project
"""

def print_banner():
    print("=" * 50)
    print("      OT Asset Discovery - LLDP Parser")
    print("=" * 50)


def create_demo_assets():
    assets = [
        {
            "Vendor": "Siemens",
            "Model": "S7-1200",
            "Protocol": "LLDP",
            "IP Address": "192.168.1.10",
            "MAC Address": "00:0E:8C:12:34:56",
            "Firmware": "V4.5",
            "Status": "Online"
        },
        {
            "Vendor": "WAGO",
            "Model": "750-8212",
            "Protocol": "LLDP",
            "IP Address": "192.168.1.20",
            "MAC Address": "00:30:DE:AA:BB:CC",
            "Firmware": "03.01",
            "Status": "Online"
        },
        {
            "Vendor": "Phoenix Contact",
            "Model": "FL SWITCH 2306",
            "Protocol": "LLDP",
            "IP Address": "192.168.1.30",
            "MAC Address": "00:A0:45:11:22:33",
            "Firmware": "2.7",
            "Status": "Online"
        }
    ]

    return assets


def display_asset(asset):
    print("\nDiscovered Asset\n")

    for key, value in asset.items():
        print(f"{key:<15}: {value}")


def main():
    print_banner()

    assets = create_demo_assets()

    for index, asset in enumerate(assets, start=1):
        print(f"\n========== Asset {index} ==========")
        display_asset(asset)


if __name__ == "__main__":
    main()