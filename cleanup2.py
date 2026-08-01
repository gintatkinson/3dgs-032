import os

# Fix assignUuid
f16 = "docs/features/feat-16-components.md"
if os.path.exists(f16):
    with open(f16, "r") as f: c = f.read()
    if "assignUuid" not in c:
        c = c.replace("class Nwi_Component {", "class Nwi_Component {\n        +String assignUuid(String namespace, String uniqueName) \"[1]\"")
    with open(f16, "w") as f: f.write(c)

# Fix missing semantic linkage in uc-13
uc13 = "docs/use-cases/uc-13-network-inventory.md"
if os.path.exists(uc13):
    with open(uc13, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if "- [ ] #61 - [Hierarchical Inventory Aggregation]" in line and "(semantic linkage:" not in line:
            lines[i] = line.strip() + " (semantic linkage: requires hierarchical logic)\n"
    with open(uc13, "w") as f:
        f.writelines(lines)

print("Cleanup2 complete.")
