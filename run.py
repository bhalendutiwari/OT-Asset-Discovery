from scripts.core.parser import PacketParser
from scripts.core.inventory import AssetInventory


PCAP_FILE = "pcaps/sample_lldp.pcap"


print("\n========================================")
print("        OT ASSET DISCOVERY")
print("========================================")


# Create packet parser

parser = PacketParser(
    PCAP_FILE
)


# Read and process PCAP

parser.load_packets()


# Get assets discovered from LLDP

discovered_assets = (
    parser.get_discovered_assets()
)


# Create asset inventory

inventory = AssetInventory()


# Add discovered assets to inventory

for asset in discovered_assets:

    inventory.add_asset(
        asset
    )


# Display inventory

inventory.show_assets()


# Display inventory summary

inventory.show_summary()


print("\n========================================")
print("       Discovery Complete")
print("========================================")