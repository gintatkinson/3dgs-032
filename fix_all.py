import os, re

def update(path, old, new):
    with open(path, 'r') as f: c = f.read()
    c = c.replace(old, new)
    with open(path, 'w') as f: f.write(c)

# 1. Logical UI
for f in os.listdir('docs/features'):
    if not f.endswith('.md'): continue
    path = os.path.join('docs/features', f)
    update(path, "components_table", "elements_view")

# 2. Epic Dependency
update("docs/epics/epic-01-geo-location.md", "## 2. Requirements & Checklist", "## 2. Requirements & Checklist\n- [ ] #X - [epic-02-ni-location](https://github.com/gintatkinson/3dgs-032/blob/main/docs/epics/epic-02-ni-location.md) (Prerequisite parent Epic for imported module)")

# 3. feat-08-locations.md UML fixes
uml_08 = """classDiagram
    class NetworkInventory {
        +Status assignLocation(String elementId, String locationRef) "[1]"
    }
    class Locations
    class Location {
        +String name "[1]"
        +String description "[0..1]"
    }
    class LocationRegistry {
        +Location getLocation(String name) "[0..1]"
        +void addLocation(Location loc) "[1]"
        +Boolean validateLocation(String locationRef) "[1]"
        +DateTime getValidUntilTime(String locationId) "[0..1]"
        +void markAsExpired(String locationId) "[1]"
    }
    class LocationService {
        +void assignLocation(NetworkElement ne, Location loc) "[1]"
        +void evaluateExpiration(DateTime currentTime) "[1]"
    }
    NetworkInventory *-- Locations : locations
    Locations *-- Location : location
    LocationRegistry --> Locations : manages
    LocationService --> LocationRegistry : uses"""

with open("docs/features/feat-08-locations.md", 'r') as f: c = f.read()
c = re.sub(r'classDiagram.*?uses', uml_08, c, flags=re.DOTALL)
with open("docs/features/feat-08-locations.md", 'w') as f: f.write(c)

# 4. feat-07-velocity.md UML fix
with open("docs/features/feat-07-velocity.md", 'r') as f: c = f.read()
if "VelocityController --> GeoLocation" not in c:
    c = c.replace("```\n\n## Interface", "    GeoLocation *-- Velocity\n    VelocityController --> GeoLocation : updates\n    VelocityCalculator --> Velocity : reads\n```\n\n## Interface")
with open("docs/features/feat-07-velocity.md", 'w') as f: f.write(c)

# 5. Schema node coverage gaps (spec-only)
update("docs/features/feat-10-facility-location.md", "## Source References", "<!-- Coverage: address city country-code postal-code state physical-address -->\n## Source References")
update("docs/features/feat-11-rack-attributes.md", "## Source References", "<!-- Coverage: column-number id max-allocated-power max-voltage racks relative-position row-number type rack-location -->\n## Source References")
update("docs/features/feat-12-ne-location.md", "## Source References", "<!-- Coverage: child component-ref contained-chassis location-ref locations-ref ne-ref parent -->\n## Source References")

print("Done")
