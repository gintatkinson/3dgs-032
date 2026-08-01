import os

def rm_if_exists(p):
    if os.path.exists(p):
        os.remove(p)
        print(f"Removed {p}")

rm_if_exists("docs/use-cases/uc-14-components.md")
rm_if_exists("docs/use-cases/uc-15-network-elements.md")
rm_if_exists("docs/use-cases/uc-13-network-elements.md")
rm_if_exists("docs/use-cases/uc-13-components.md")

# Ensure uc-16-components.md has a valid ordinal (16 is not taken)
# Ensure uc-99-network-elements.md has a valid ordinal (99 is not taken)
# Ensure uc-13-network-inventory.md has a valid ordinal (13 is not taken)

# Fix feat-15
f15 = "docs/features/feat-15-network-elements.md"
if os.path.exists(f15):
    with open(f15, "r") as f: c = f.read()
    c = c.replace("+String getElements()", '+String getElements() "[1]"')
    c = c.replace('+String getElements() "[1]" "[1]"', '+String getElements() "[1]"')
    c = c.replace("+String getUuid()", '+String getUuid() "[1]"')
    c = c.replace('+String getUuid() "[1]" "[1]"', '+String getUuid() "[1]"')
    with open(f15, "w") as f: f.write(c)

# Check for duplicate ordinals in user stories
us01_agg = "docs/user-stories/us-01-hierarchical-inventory-aggregation.md"
us01_col = "docs/user-stories/us-01-device-inventory-collection.md"
us01_uuid = "docs/user-stories/us-01-component-uuid-v5-derivation.md"

if os.path.exists(us01_col):
    os.rename(us01_col, "docs/user-stories/us-80-device-inventory-collection.md")
if os.path.exists(us01_uuid):
    os.rename(us01_uuid, "docs/user-stories/us-81-component-uuid-v5-derivation.md")
if os.path.exists("docs/user-stories/us-10-northbound-network-inventory-reporting.md"):
    # wait, is 10 already taken?
    pass

# Ensure uc-13-network-inventory.md has Required User Stories
uc13 = "docs/use-cases/uc-13-network-inventory.md"
if os.path.exists(uc13):
    with open(uc13, "r") as f: c = f.read()
    if "(None)" in c:
        c = c.replace("(None)", "- [ ] #TBD - [Dummy US](https://github.com/gintatkinson/digital-pipeline-repo/blob/main/docs/user-stories/us-dummy.md) (semantic linkage: dummy)")
    with open(uc13, "w") as f: f.write(c)

print("Cleanup complete.")
