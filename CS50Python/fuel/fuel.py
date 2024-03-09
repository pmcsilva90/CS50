while True:
    try:
        gauge = input("Fraction: ")

        x, y = gauge.split(sep="/")

        x = int(x)
        y = int(y)
        break
    except ValueError:
        print("")
        pass


percent = x / y * 100

print(f"{percent:.0f}%")
