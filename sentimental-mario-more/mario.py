from cs50 import get_int

height = get_int("Height: ")

while height < 0 or height > 8:
    height = get_int("Height: ")

for i in range(height):
    for j in range(i + 1):
        print()
        print("#", end="")
    print()
