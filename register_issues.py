import subprocess
import re
import os

mapping = {
    'docs/use-cases/uc-06-geo-location-grouping.md': 24,
    'docs/use-cases/uc-07-reference-frame.md': 25,
    'docs/use-cases/uc-08-geodetic-system.md': 26,
    'docs/use-cases/uc-09-location-choice.md': 27,
    'docs/use-cases/uc-10-location-ellipsoid.md': 28,
    'docs/use-cases/uc-11-location-cartesian.md': 29,
    'docs/use-cases/uc-12-velocity.md': 30
}

def inject_issue_id(filepath, issue_id):
    with open(filepath, 'r') as f:
        content = f.read()
    if 'issue_id:' not in content:
        content = content.replace('---\n\n', f'issue_id: {issue_id}\n---\n\n', 1)
        if 'issue_id:' not in content:
            # handle case where no extra newline after ---
            content = content.replace('\n---\n# ', f'\nissue_id: {issue_id}\n---\n\n# ', 1)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated {filepath} with issue_id: {issue_id}")

for filepath, issue_id in mapping.items():
    inject_issue_id(filepath, issue_id)

new_usecases = [
    'docs/use-cases/uc-01-locations.md',
    'docs/use-cases/uc-02-geo-location.md',
    'docs/use-cases/uc-03-facility-location.md',
    'docs/use-cases/uc-04-rack-attributes.md',
    'docs/use-cases/uc-05-ne-location.md'
]

for filepath in new_usecases:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'title:\s*"([^"]+)"', content)
    title = title_match.group(1) if title_match else "Use Case"
    
    print(f"Creating issue for {filepath}: {title}")
    result = subprocess.run([
        './skills/spec-orchestrator/scripts/create_issue.sh',
        filepath,
        'use-case',
        title
    ], capture_output=True, text=True)
    
    print(result.stdout)
    if result.returncode != 0:
        print("ERROR:", result.stderr)
        continue
        
    # The output of gh issue create is a URL like https://github.com/user/repo/issues/42
    url_match = re.search(r'https://github.com/[^/]+/[^/]+/issues/(\d+)', result.stdout)
    if url_match:
        issue_id = int(url_match.group(1))
        inject_issue_id(filepath, issue_id)
    else:
        print("Could not find issue URL in output")

