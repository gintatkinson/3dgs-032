import sys, os, re
sys.path.insert(0, 'skills/spec-orchestrator/parity_auditor/src')
from parity_auditor.cli import _extract_issue_id_from_frontmatter

missing_specs = []
for issue_number in [31, 32, 33, 34, 35]:
    found = False
    for fname in os.listdir('docs/features'):
        if not fname.endswith('.md'): continue
        with open(os.path.join('docs/features', fname)) as f:
            content = f.read()
        frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if frontmatter_match:
            if _extract_issue_id_from_frontmatter(frontmatter_match.group(1), issue_number):
                found = True
                break
    if not found:
        print(f"Missing {issue_number}")
