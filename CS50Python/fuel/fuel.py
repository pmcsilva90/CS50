gauge = input("Fraction: ")

x, y = gauge.split(sep="/")

while True:
    try:
        x = int(x)
        y = int(y)
        break
    except ValueError:
        pass


percent = x / y * 100

print(f"{percent:.0f}%")
