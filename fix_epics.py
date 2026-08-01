import re
f1 = '/Users/perkunas/jail/3dgs-032/docs/epics/epic-02-ni-location.md'
f2 = '/Users/perkunas/jail/3dgs-032/docs/epics/epic-01-geo-location.md'

with open(f1, 'r') as f:
    c1 = f.read()
c1 = c1.replace('(semantic linkage justification)', '(Realizes Epic component)')
with open(f1, 'w') as f:
    f.write(c1)

with open(f2, 'r') as f:
    c2 = f.read()
c2 = c2.replace('(semantic linkage justification)', '(Realizes Epic component)')

issue_map = {
    'feat-01-geo-location.md': '6',
    'feat-02-reference-frame.md': '8',
    'feat-03-geodetic-system.md': '9',
    'feat-04-location-choice.md': '11',
    'feat-05-location-ellipsoid.md': '12',
    'feat-06-location-cartesian.md': '14',
    'feat-07-velocity.md': '15',
}

for filename, issue_id in issue_map.items():
    c2 = re.sub(r'#\[IssueID\](.*?)(?=' + re.escape(filename) + ')', r'#' + issue_id + r'\1', c2)

with open(f2, 'w') as f:
    f.write(c2)
