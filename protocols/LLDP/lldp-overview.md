# Understanding LLDP for OT Asset Discovery

## What is LLDP?

Link Layer Discovery Protocol (LLDP) is an IEEE 802.1AB standard that allows network devices to advertise their identity and capabilities to directly connected neighbors.

LLDP operates at Layer 2 of the OSI model and is vendor-neutral, making it useful in environments containing equipment from multiple manufacturers.

---

## Why is LLDP Important in OT?

In Operational Technology (OT) environments, asset visibility is one of the biggest security challenges.

When supported by a device, LLDP can provide valuable information such as:

- Device Name
- Device Model
- Manufacturer
- Software/Firmware Version
- Port Information
- Management Address

This enables passive asset discovery without actively scanning industrial devices.

---

## Advantages

- Passive discovery
- No impact on PLC operation
- Vendor-neutral
- Useful for network documentation
- Helps identify unmanaged devices

---

## Limitations

- Not all OT devices support LLDP.
- Some vendors advertise only limited information.
- Older PLCs may not implement LLDP.
- LLDP only discovers directly connected neighbors.

---

## Typical OT Devices Supporting LLDP

- Industrial Ethernet Switches
- Some Siemens PLCs
- Engineering Workstations
- Industrial PCs
- Managed Network Infrastructure

---

## Next Steps

Future documentation will include:

- LLDP Packet Structure
- TLV Analysis
- Wireshark Examples
- Vendor Fingerprinting
- Python Parser
