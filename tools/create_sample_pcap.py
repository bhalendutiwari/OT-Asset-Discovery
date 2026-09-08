from scapy.all import Ether, Raw, wrpcap


OUTPUT_FILE = "pcaps/sample_lldp.pcap"


def create_chassis_tlv(mac_address):

    return (
        bytes.fromhex("02 07")
        + bytes([4])
        + bytes.fromhex(
            mac_address.replace(":", " ")
        )
    )


def create_port_tlv(port_name):

    port_value = (
        bytes([5])
        + port_name.encode("utf-8")
    )

    length = len(port_value)

    header = (
        (2 << 9)
        | length
    )

    return header.to_bytes(
        2,
        byteorder="big"
    ) + port_value


def create_ttl_tlv(ttl=120):

    header = (
        (3 << 9)
        | 2
    )

    return (
        header.to_bytes(
            2,
            byteorder="big"
        )
        + ttl.to_bytes(
            2,
            byteorder="big"
        )
    )


def create_system_name_tlv(name):

    value = name.encode("utf-8")

    header = (
        (5 << 9)
        | len(value)
    )

    return (
        header.to_bytes(
            2,
            byteorder="big"
        )
        + value
    )


def create_system_description_tlv(description):

    value = description.encode("utf-8")

    header = (
        (6 << 9)
        | len(value)
    )

    return (
        header.to_bytes(
            2,
            byteorder="big"
        )
        + value
    )


def create_management_address_tlv(ip_address):

    ip_bytes = bytes(
        int(part)
        for part in ip_address.split(".")
    )

    value = (
        bytes([5])
        + bytes([1])
        + ip_bytes
    )

    header = (
        (8 << 9)
        | len(value)
    )

    return (
        header.to_bytes(
            2,
            byteorder="big"
        )
        + value
    )


def create_end_tlv():

    return bytes.fromhex(
        "00 00"
    )


def create_lldp_payload(
    mac_address,
    port_name,
    system_name,
    system_description,
    management_ip
):

    payload = (
        create_chassis_tlv(mac_address)
        + create_port_tlv(port_name)
        + create_ttl_tlv()
        + create_system_name_tlv(system_name)
        + create_system_description_tlv(
            system_description
        )
        + create_management_address_tlv(
            management_ip
        )
        + create_end_tlv()
    )

    return payload


def create_lldp_packet(
    src_mac,
    port_name,
    system_name,
    system_description,
    management_ip
):

    payload = create_lldp_payload(
        src_mac,
        port_name,
        system_name,
        system_description,
        management_ip
    )

    packet = (
        Ether(
            src=src_mac,
            dst="01:80:c2:00:00:0e",
            type=0x88CC
        )
        / Raw(
            load=payload
        )
    )

    return packet


def main():

    plc_packet = create_lldp_packet(
        src_mac="00:11:22:33:44:55",
        port_name="GigabitEthernet1/0/1",
        system_name="PLC-01",
        system_description="Siemens S7-1500 PLC",
        management_ip="192.168.1.10"
    )

    switch_packet = create_lldp_packet(
        src_mac="00:AA:BB:CC:DD:EE",
        port_name="GigabitEthernet1/0/24",
        system_name="SW-01",
        system_description="Industrial Ethernet Switch",
        management_ip="192.168.1.1"
    )

    packets = []

    # Simulate three LLDP advertisements
    # from each device.

    for _ in range(3):

        packets.append(
            plc_packet
        )

        packets.append(
            switch_packet
        )

    wrpcap(
        OUTPUT_FILE,
        packets
    )

    print(
        f"Created PCAP: {OUTPUT_FILE}"
    )

    print(
        f"Packets written: {len(packets)}"
    )


if __name__ == "__main__":
    main()