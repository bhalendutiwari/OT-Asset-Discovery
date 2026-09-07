from scripts.lldp.lldp_parser import LLDPParser


parser = LLDPParser()


asset = parser.parse(None)


print("\nDiscovered Asset")
print("================")


for key, value in asset.items():

    print(
        f"{key:<25}: {value}"
    )