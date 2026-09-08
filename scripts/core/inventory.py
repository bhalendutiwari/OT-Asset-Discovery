from scripts.core.asset import OTAsset


class AssetInventory:

    def __init__(self):
        self.assets = []

    def add_asset(self, asset):

        # Support the new OTAsset model.
        if isinstance(asset, OTAsset):

            chassis_id = asset.chassis_id

            if not chassis_id:

                asset.record_observation()

                self.assets.append(asset)

                return

            for existing_asset in self.assets:

                if (
                    isinstance(existing_asset, OTAsset)
                    and existing_asset.chassis_id == chassis_id
                ):

                    existing_asset.record_observation()

                    return

            # The parser already records the first
            # observation, so add the asset directly.
            self.assets.append(asset)

            return

        # Preserve support for the original
        # dictionary-based inventory.

        chassis_id = asset.get("chassis_id")

        if not chassis_id:

            asset["observation_count"] = 1

            self.assets.append(asset)

            return

        for existing_asset in self.assets:

            if (
                isinstance(existing_asset, dict)
                and existing_asset.get("chassis_id")
                == chassis_id
            ):

                existing_asset["observation_count"] += 1

                return

        asset["observation_count"] = 1

        self.assets.append(asset)

    def total_assets(self):

        return len(self.assets)

    def unique_vendors(self):

        vendors = set()

        for asset in self.assets:

            if isinstance(asset, OTAsset):

                continue

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

            if isinstance(asset, OTAsset):

                asset_data = asset.to_dict()

            else:

                asset_data = asset

            for key, value in asset_data.items():

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