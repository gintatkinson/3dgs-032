import re, os

# 1. Fix missing local specification files by adding `issue_id: XX` to frontmatter
mapping = {
    "docs/features/feat-08-locations.md": "31",
    "docs/features/feat-09-ni-geo-location.md": "32",
    "docs/features/feat-10-facility-location.md": "33",
    "docs/features/feat-11-rack-attributes.md": "34",
    "docs/features/feat-12-ne-location.md": "35",
}

for file, issue in mapping.items():
    with open(file, 'r') as f:
        content = f.read()
    if not re.search(r'^issue_id:\s*\d+', content, flags=re.MULTILINE):
        content = re.sub(r'^(title:.*?)\n', f'\\1\nissue_id: {issue}\n', content, count=1, flags=re.MULTILINE)
        with open(file, 'w') as f:
            f.write(content)

# 2. Epic dependency
epic_path = "docs/epics/epic-01-geo-location.md"
with open(epic_path, 'r') as f: c = f.read()
if "epic-02-ni-location.md" not in c:
    c = c.replace("## 2. Requirements & Checklist", "## 2. Requirements & Checklist\n- [ ] #36 - [epic-02-ni-location](https://github.com/gintatkinson/3dgs-032/blob/main/docs/epics/epic-02-ni-location.md) (Prerequisite parent Epic for imported module)")
with open(epic_path, 'w') as f: f.write(c)

print("Fixed.")
