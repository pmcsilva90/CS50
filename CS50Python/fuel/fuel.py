gauge = input("Fraction: ")

x, y = gauge.split(sep="/")
x = int(x)
y = int(y)

percent = x / y * 100

print(percent + "%")
