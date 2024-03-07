# Convert camel case to snake case

var = input("camelCase: ")

char_count = 0

for c in var:
    char_count += 1
    if c.isupper():
        c = c.lower()
        print("_" + c, end="")
    else:
        print(c, end="")
print()
