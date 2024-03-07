var = input("camelCase: ")

char_count = 0

for c in var:
    char_count += 1
    if c.isupper():
        c = c.lower()
        print(var[char_count:] + "_", end="")

print(var[-(len(var) - char_count):])

