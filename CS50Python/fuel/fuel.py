while True:
    try:
        gauge = input("Fraction: ")

        x, y = gauge.split(sep="/")

        x = int(x)
        y = int(y)
        percent = x / y * 100

        break
    except (ValueError, ZeroDivisionError):
        print("Invalid fraction")
        pass



if percent >= 99:
    print("F")
elif percent <= 1:
    print("E")
else:
    print(f"{percent:.0f}%")
