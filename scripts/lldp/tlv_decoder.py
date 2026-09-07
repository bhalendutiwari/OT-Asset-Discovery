class LLDPDecoder:

    TLV_TYPES = {
        0: "End of LLDPDU",
        1: "Chassis ID",
        2: "Port ID",
        3: "TTL",
        4: "Port Description",
        5: "System Name",
        6: "System Description",
        7: "System Capabilities",
        8: "Management Address"
    }

    CHASSIS_ID_SUBTYPES = {
        1: "Chassis Component",
        2: "Interface Alias",
        3: "Port Component",
        4: "MAC Address",
        5: "Network Address",
        6: "Interface Name",
        7: "Locally Assigned"
    }

    PORT_ID_SUBTYPES = {
        1: "Interface Alias",
        2: "Port Component",
        3: "MAC Address",
        4: "Network Address",
        5: "Interface Name",
        6: "Agent Circuit ID",
        7: "Locally Assigned"
    }

    def decode_type(self, tlv_type):
        return self.TLV_TYPES.get(
            tlv_type,
            "Unknown"
        )

    def decode_header(self, header):

        tlv_type = header >> 9
        tlv_length = header & 0x01FF

        return tlv_type, tlv_length

    def decode(self, data):

        if len(data) < 2:
            raise ValueError(
                "TLV data must contain at least 2 bytes"
            )

        header = int.from_bytes(
            data[:2],
            byteorder="big"
        )

        tlv_type, tlv_length = self.decode_header(
            header
        )

        if len(data) < 2 + tlv_length:
            raise ValueError(
                "TLV data is shorter than declared length"
            )

        value = data[2:2 + tlv_length]

        return {
            "type": tlv_type,
            "name": self.decode_type(tlv_type),
            "length": tlv_length,
            "value": value
        }

    def decode_all(self, data):

        tlvs = []
        offset = 0

        while offset + 2 <= len(data):

            header = int.from_bytes(
                data[offset:offset + 2],
                byteorder="big"
            )

            tlv_type, tlv_length = self.decode_header(
                header
            )

            if offset + 2 + tlv_length > len(data):
                raise ValueError(
                    "Incomplete TLV data"
                )

            value_start = offset + 2
            value_end = value_start + tlv_length

            value = data[value_start:value_end]

            tlv = {
                "type": tlv_type,
                "name": self.decode_type(tlv_type),
                "length": tlv_length,
                "value": value
            }

            tlvs.append(tlv)

            offset = value_end

            if tlv_type == 0:
                break

        return tlvs

    def decode_chassis_id(self, value):

        if len(value) < 2:
            raise ValueError(
                "Chassis ID value must contain a subtype and identifier"
            )

        subtype = value[0]

        subtype_name = self.CHASSIS_ID_SUBTYPES.get(
            subtype,
            "Unknown"
        )

        identifier = value[1:]

        if subtype == 4 and len(identifier) == 6:

            identifier_value = ":".join(
                f"{byte:02x}"
                for byte in identifier
            )

        else:

            try:
                identifier_value = identifier.decode(
                    "utf-8"
                )
            except UnicodeDecodeError:
                identifier_value = identifier.hex()

        return {
            "subtype": subtype,
            "subtype_name": subtype_name,
            "identifier": identifier_value
        }

    def decode_port_id(self, value):

        if len(value) < 2:
            raise ValueError(
                "Port ID value must contain a subtype and identifier"
            )

        subtype = value[0]

        subtype_name = self.PORT_ID_SUBTYPES.get(
            subtype,
            "Unknown"
        )

        identifier = value[1:]

        if subtype == 3 and len(identifier) == 6:

            identifier_value = ":".join(
                f"{byte:02x}"
                for byte in identifier
            )

        else:

            try:
                identifier_value = identifier.decode(
                    "utf-8"
                )
            except UnicodeDecodeError:
                identifier_value = identifier.hex()

        return {
            "subtype": subtype,
            "subtype_name": subtype_name,
            "identifier": identifier_value
        }

    def decode_ttl(self, value):

        if len(value) != 2:
            raise ValueError(
                "TTL value must contain exactly 2 bytes"
            )

        ttl = int.from_bytes(
            value,
            byteorder="big"
        )

        return ttl

    def decode_system_name(self, value):

        try:
            return value.decode("utf-8")

        except UnicodeDecodeError:
            return value.hex()

    def decode_system_description(self, value):

        try:
            return value.decode("utf-8")

        except UnicodeDecodeError:
            return value.hex()