from cs50 import get_int

height = -1

while height < 0 and height > 8:
    height = get_int("Height: ")

for i in range(height):
    for j in range(i + 1):
        print("#", end="")
