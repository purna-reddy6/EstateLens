# Data Model

Each property listing rendered on the map and list panel carries the following
fields, consumed by both the Leaflet map and the Chart.js radar visualization.

## Listing

| Field | Type | Notes |
|-------|------|-------|
| `id` | string | Unique listing id |
| `title` | string | Display name |
| `type` | `sale` \| `rent` | Drives pin colour and filtering |
| `price` | number | INR |
| `area` | number | Square feet |
| `furnishing` | string | Furnished / semi / unfurnished |
| `coordinates` | [lat, lng] | Pin position |
| `boundary` | [[lat, lng], …] | Polygon drawn on the map |
| `photos` | string[] | Image URLs |

## Realest Trust Report

Verified attributes shown in the slide-in panel: legal status, water source,
power backup, and ownership verification.

## Liveability Index

Four 0–10 scores visualized as a radar chart: **Walkability**, **Safety**,
**Noise**, and **Connectivity**.
