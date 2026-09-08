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

            vendor = asset.get("Vendor")

            if vendor:
                vendors.add(vendor)

        return vendors

    def show_assets(self):

        print("\n====================================")
        print("OT Asset Inventory")
        print("====================================")

        if not self.assets:
            print("No assets discovered.")
            return

        for index, asset in enumerate(
            self.assets,
            start=1
        ):

            print(
                f"\nAsset {index}"
            )
            print("------------------------------------")

            for key, value in asset.items():

                print(
                    f"{key:<20}: {value}"
                )

    def show_summary(self):

        print("\n====================================")
        print("OT Asset Inventory Summary")
        print("====================================")

        print(
            f"Total Assets   : {self.total_assets()}"
        )

        print(
            f"Unique Vendors : {len(self.unique_vendors())}"
        )

        vendors = self.unique_vendors()

        if vendors:

            print(
                "Vendor List    :",
                ", ".join(sorted(vendors))
            )

        else:

            print(
                "Vendor List    : None"
            )