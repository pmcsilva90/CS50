gauge = input("Fraction: ")

x, y = gauge.split(sep="/")

percent = x / y * 100

print(percent + "%")
