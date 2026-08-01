import re

mapping = {
    "docs/features/feat-08-locations.md": "#31",
    "docs/features/feat-09-ni-geo-location.md": "#32",
    "docs/features/feat-10-facility-location.md": "#33",
    "docs/features/feat-11-rack-attributes.md": "#34",
    "docs/features/feat-12-ne-location.md": "#35",
}

for file, issue in mapping.items():
    with open(file, 'r') as f:
        content = f.read()
    
    # if issue is not already present, insert it
    if not re.search(r'^issue:\s*".*?"', content, flags=re.MULTILINE):
        content = re.sub(r'^(title:.*?)\n', f'\\1\nissue: "{issue}"\n', content, count=1, flags=re.MULTILINE)
        with open(file, 'w') as f:
            f.write(content)
        print(f"Updated {file}")
