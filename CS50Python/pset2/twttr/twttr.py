input = input("Input: ")

print("Output: ", end="")

for c in input:
    if c.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("", end="")
    else:
        print(c, end="")
print()
