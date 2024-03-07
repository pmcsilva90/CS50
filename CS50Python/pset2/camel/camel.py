var = input("camelCase: ")

char_counter = 0

for c in var:
    char_counter += 1
    if c.isupper():
        c = c.lower()
        for _ in range(char_counter):
            print(c + "_", end="")
    print(c )

