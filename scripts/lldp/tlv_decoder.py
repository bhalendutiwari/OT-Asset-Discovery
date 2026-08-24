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

    def decode_type(self, tlv_type):
        return self.TLV_TYPES.get(tlv_type, "Unknown")

    def decode_header(self, header):

        tlv_type = header >> 9
        tlv_length = header & 0x01FF

        return tlv_type, tlv_length

    def decode(self, data):

        if len(data) < 2:
            raise ValueError("TLV data must contain at least 2 bytes")

        header = int.from_bytes(data[:2], byteorder="big")

        tlv_type, tlv_length = self.decode_header(header)

        if len(data) < 2 + tlv_length:
            raise ValueError("TLV data is shorter than declared length")

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

            tlv_type, tlv_length = self.decode_header(header)

            if offset + 2 + tlv_length > len(data):
                raise ValueError("Incomplete TLV data")

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