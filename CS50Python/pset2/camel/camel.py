var = input("camelCase: ")

for c in var:
    if c == c.isupper():
        c = c.lower()
        print()
