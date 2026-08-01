import re
import yaml

with open('docs/features/feat-08-locations.md', 'r') as f:
    content = f.read()

frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
if frontmatter_match:
    fm_text = frontmatter_match.group(1)
    data = yaml.safe_load(fm_text)
    print(data.get("issue_id") == 31)
else:
    print("NO MATCH")
