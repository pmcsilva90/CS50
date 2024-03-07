from cs50 import get_int

#height = get_int("Height: ")

#while height < 1 or height > 8:
#    height = get_int("Height: ")

#for i in range(height):
#    for _ in range(height - i - 1):
#        print(" ", end="")
#    for _ in range(i + 1):
#        print("#", end="")
#    print("  ", end="")
#    for _ in range(i + 1):
#        print("#", end="")
#    print()

while True:
    height = get_int("Height: ")
    if 1 <= height <= 8:
        break

for i in range(height):
    print(" " * (height - i - 1), end="")
    print("#" * (i + 1), end="")
    print("  ", end="")
    print("#" * (i + 1), end="")
    print()
