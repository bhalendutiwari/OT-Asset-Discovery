# LLDP TLV Analysis

## What is a TLV?

TLV stands for **Type-Length-Value**.

Instead of using fixed packet fields, LLDP stores information as a sequence of TLVs. Each TLV describes one characteristic of the transmitting device.

```
+--------+---------+----------------+
| Type   | Length  | Value          |
+--------+---------+----------------+
```

---

# Why TLVs Matter

Each TLV provides information that can help identify industrial devices without sending active probes.

Examples include:

- Device identity
- Switch port
- Firmware version
- Management IP
- System capabilities

---

# Mandatory TLVs

## 1. Chassis ID

Purpose

Identifies the transmitting device.

Common Values

- MAC Address
- Chassis Component
- Network Address

### OT Security Importance

Acts as the primary identifier for an industrial asset.

---

## 2. Port ID

Purpose

Identifies the physical or logical interface.

Examples

- Port 1
- X1 P1
- GigabitEthernet1/0/1

### OT Security Importance

Useful for topology mapping.

---

## 3. Time To Live (TTL)

Purpose

Specifies how long neighboring devices should retain the information.

Typical Value

120 seconds

---

# Optional TLVs

## System Name

Often contains:

- PLC Name
- Switch Name
- Engineering Station Name

Example

```
PLC-Line-01
```

---

## System Description

May contain

- Vendor
- Product Model
- Firmware Version
- Operating System

Example

```
Siemens S7-1200 CPU1214C Firmware V4.5
```

---

## System Capabilities

Indicates what the device can perform.

Examples

- Bridge
- Router
- Station

---

## Management Address

Contains the IP address used for device management.

Example

```
192.168.1.10
```

---

# OT Analyst Notes

The most valuable TLVs during passive asset discovery are:

- Chassis ID
- System Name
- System Description
- Management Address

These four TLVs often provide enough information to identify an industrial asset without active scanning.

---

# Conclusion

TLVs make LLDP one of the richest passive discovery protocols available in industrial Ethernet networks. However, because vendor implementations differ, LLDP should be combined with additional industrial protocols for complete asset visibility.
