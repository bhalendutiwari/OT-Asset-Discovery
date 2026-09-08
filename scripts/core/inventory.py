class AssetInventory:

    def __init__(self):
        self.assets = []

    def add_asset(self, asset):

        chassis_id = asset.get("chassis_id")

        # If there is no chassis ID, treat the asset
        # as a separate observation.
        if not chassis_id:

            asset["observation_count"] = 1
            self.assets.append(asset)
            return

        # Check whether this asset has already
        # been discovered.
        for existing_asset in self.assets:

            if existing_asset.get("chassis_id") == chassis_id:

                existing_asset["observation_count"] += 1

                return

        # New asset discovered.
        asset["observation_count"] = 1

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

            print(
                "------------------------------------"
            )

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