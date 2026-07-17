# LLDP Packet Structure

## Overview

An LLDP packet is transmitted using Ethernet frames and contains a sequence of Type-Length-Value (TLV) fields. Each TLV provides specific information about the transmitting device.

Understanding these fields helps identify industrial devices without actively scanning the network.

---

# Ethernet Header

| Field | Purpose |
|--------|---------|
| Destination MAC | LLDP Multicast Address (01:80:C2:00:00:0E) |
| Source MAC | MAC Address of the transmitting device |
| EtherType | 0x88CC (Identifies LLDP) |

---

# LLDP TLVs

## 1. Chassis ID

Identifies the physical device.

Typical values include:

- MAC Address
- Chassis Serial Number
- Device Identifier

### OT Security Value

Useful for uniquely identifying PLCs, switches and industrial devices.

---

## 2. Port ID

Identifies the transmitting interface.

Examples:

- Port 1
- GigabitEthernet1/0/1
- X1 P1

### OT Security Value

Helps map network topology.

---

## 3. Time To Live (TTL)

Defines how long neighboring devices should keep the information.

Typical value:

120 seconds

---

## 4. System Name

Human-readable device name.

Example:

```
PLC-Line-1
```

### OT Security Value

Often reveals the function of the device.

---

## 5. System Description

Contains detailed information.

May include:

- Vendor
- Device Model
- Firmware Version
- Operating System

### OT Security Value

One of the most valuable fields for passive asset identification.

---

## 6. System Capabilities

Describes device capabilities.

Examples:

- Bridge
- Router
- Station
- Telephone

---

## 7. Management Address

Provides the management IP address.

Example:

```
192.168.10.20
```

### OT Security Value

Allows security teams to associate a device with its management interface.

---

## 8. End of LLDPDU

Marks the end of the LLDP packet.

---

# Summary

LLDP provides valuable metadata that enables passive OT asset discovery without generating active network traffic.

When available, it is one of the safest methods for identifying industrial assets.


# Field Observations

During my laboratory analysis:

- Siemens S7-1200 devices advertise detailed LLDP information including model, firmware and system description.
- Some WAGO devices may not transmit LLDP packets, limiting passive identification using this protocol.
- LLDP support varies between industrial vendors and device families.

This reinforces the importance of combining LLDP with other industrial protocols such as Profinet DCP, EtherNet/IP, Modbus TCP and SNMP for comprehensive OT asset discovery.
