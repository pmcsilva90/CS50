input = input("Input: ")

print("Output: ", end="")

for c in input:
    if c in ['a', 'e', 'i', 'o', 'u']:
        print("", end="")
    else:
        print(c, end="")
print()
