var = input("camelCase: ")

for c in var:
    if c.isupper():
        c = c.lower()
        print()
