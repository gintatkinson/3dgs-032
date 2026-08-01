with open("docs/use-cases/uc-03-facility-location.md", 'r') as f:
    content = f.read()

extra_flows = """
- **5c. Missing Address (Branches from Basic Flow step 2):**
  1. LocationRegistry detects that the address is invalid.
  2. LocationRegistry aborts the transaction.

- **5d. Missing City (Branches from Basic Flow step 2):**
  1. LocationRegistry detects that the city is invalid.
  2. LocationRegistry aborts the transaction.

- **5e. Missing Country Code (Branches from Basic Flow step 2):**
  1. LocationRegistry detects that the country code is invalid.
  2. LocationRegistry aborts the transaction.

- **5f. Missing Postal Code (Branches from Basic Flow step 2):**
  1. LocationRegistry detects that the postal code is invalid.
  2. LocationRegistry aborts the transaction.

- **5g. Missing State (Branches from Basic Flow step 2):**
  1. LocationRegistry detects that the state is invalid.
  2. LocationRegistry aborts the transaction.

- **5h. Missing Physical Address (Branches from Basic Flow step 2):**
  1. LocationRegistry detects that the physical address is invalid.
  2. LocationRegistry aborts the transaction.
"""
content = content.replace("## 6. Postconditions (Guarantees)", extra_flows + "\n## 6. Postconditions (Guarantees)")

with open("docs/use-cases/uc-03-facility-location.md", 'w') as f:
    f.write(content)

print("Fixed")
