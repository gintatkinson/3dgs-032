---
title: "Shared Type Registry"
type: "registry"
module: "ietf-yang-types"
---

# Shared Type Registry: ietf-yang-types

This module contains generally useful derived YANG data types. Since it is a utility module, no Epics or Features are generated for it. The types below serve as shared DataTypes/UML Primitives for other functional modules.

## Data Types

| Type Name | Base Type | Description / Notes |
|---|---|---|
| `counter32` | `uint32` | Monotonically increasing non-negative integer (up to 2^32-1). |
| `zero-based-counter32` | `counter32` | A counter32 with an initial value of zero. |
| `counter64` | `uint64` | Monotonically increasing non-negative integer (up to 2^64-1). |
| `zero-based-counter64` | `counter64` | A counter64 with an initial value of zero. |
| `gauge32` | `uint32` | Non-negative integer that may increase or decrease (up to 2^32-1). |
| `gauge64` | `uint64` | Non-negative integer that may increase or decrease (up to 2^64-1). |
| `object-identifier` | `string` | Registration-hierarchical-name tree identifier (OIDs). |
| `object-identifier-128` | `object-identifier` | OIDs restricted to 128 sub-identifiers. |
| `date-and-time` | `string` | Profile of ISO 8601 representation of dates and times. |
| `date` | `string` | Time-interval of the length of a day (24 hours). |
| `date-no-zone` | `date` | Date without time zone offset information. |
| `time` | `string` | Instance of time of zero duration recurring every day. |
| `time-no-zone` | `time` | Time without time zone offset information. |
| `hours32` | `int32` | Period of time measured in units of hours. |
| `minutes32` | `int32` | Period of time measured in units of minutes. |
| `seconds32` | `int32` | Period of time measured in units of seconds. |
| `centiseconds32` | `int32` | Period of time measured in units of 10^-2 seconds. |
| `milliseconds32` | `int32` | Period of time measured in units of 10^-3 seconds. |
| `microseconds32` | `int32` | Period of time measured in units of 10^-6 seconds. |
| `microseconds64` | `int64` | Period of time measured in units of 10^-6 seconds. |
| `nanoseconds32` | `int32` | Period of time measured in units of 10^-9 seconds. |
| `nanoseconds64` | `int64` | Period of time measured in units of 10^-9 seconds. |
| `timeticks` | `uint32` | Time modulo 2^32 in hundredths of a second. |
| `timestamp` | `timeticks` | Value of an associated timeticks schema node. |
| `phys-address` | `string` | Media/physical-level address (sequence of octets). |
| `mac-address` | `string` | 48-bit IEEE 802 Media Access Control (MAC) address. |
| `xpath1.0` | `string` | XPATH 1.0 expression. |
| `hex-string` | `string` | Hexadecimal string (octets separated by colons). |
| `uuid` | `string` | Universally Unique IDentifier (RFC 9562). |
| `dotted-quad` | `string` | Unsigned 32-bit number expressed in dotted-quad notation. |
| `language-tag` | `string` | Language tag according to RFC 5646 (BCP 47). |
| `yang-identifier` | `string` | YANG identifier string. |

## Source References
Structural Schema: [ietf-yang-types@2025-12-22.yang](file:///Users/perkunas/jail/3dgs-032/schema/ietf-yang-types@2025-12-22.yang)
