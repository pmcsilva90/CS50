# Convert camel case to snake case

var = input("camelCase: ")

for c in var:
    if c.isupper():
        print("_" + c.lower(), end="")
    else:
        print(c, end="")
print()
