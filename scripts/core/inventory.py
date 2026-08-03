class AssetInventory:

    def __init__(self):
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def total_assets(self):
        return len(self.assets)

    def unique_vendors(self):
        vendors = set()

        for asset in self.assets:
            vendors.add(asset["Vendor"])

        return vendors

    def show_summary(self):

        print("\n====================================")
        print("OT Asset Inventory Summary")
        print("====================================")

        print(f"Total Assets : {self.total_assets()}")
        print(f"Unique Vendors : {len(self.unique_vendors())}")
        print("Vendor List :", ", ".join(sorted(self.unique_vendors())))