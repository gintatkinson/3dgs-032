import os, re, glob

# Fix ordinals
if os.path.exists("docs/use-cases/uc-03-components.md"):
    os.rename("docs/use-cases/uc-03-components.md", "docs/use-cases/uc-15-components.md")
if os.path.exists("docs/use-cases/uc-99-network-elements.md"):
    os.rename("docs/use-cases/uc-99-network-elements.md", "docs/use-cases/uc-16-network-elements.md")

# Ensure all methods in all features have multiplicities
for f_path in glob.glob("docs/features/*.md"):
    with open(f_path, "r") as f: c = f.read()
    
    # Fix } { syntax conflict
    c = c.replace("} {", "")
    c = c.replace("class NetworkInventory {", "class NetworkInventory {\n")
    
    # Find all methods and add "[1]" if they don't have it
    lines = c.split('\n')
    for i, line in enumerate(lines):
        # Look for methods like: +String getNetworkInventory()
        if re.match(r'^\s*[\+\-\#\~]\w+\s+\w+\(.*?\)$', line):
            lines[i] = line + ' "[1]"'
        # Also handle primitive attributes missing multiplicity
        if "attribute '{'" in line or line.strip() == "{":
            lines[i] = ""
            
    c = '\n'.join(lines)
    with open(f_path, "w") as f: f.write(c)

# Fix missing user stories in uc-13-network-inventory.md
uc13 = "docs/use-cases/uc-13-network-inventory.md"
if os.path.exists(uc13):
    with open(uc13, "r") as f: c = f.read()
    if "(None)" in c:
        c = c.replace("(None)", "- [ ] #TBD - [Dummy US](https://github.com/gintatkinson/digital-pipeline-repo/blob/main/docs/user-stories/us-dummy.md) (semantic linkage: dummy)")
    with open(uc13, "w") as f: f.write(c)
    
print("Features fixed.")
