expression = input("Expression: ")

x, y, z = expression.split(" ")

x = int(x)
z = int(z)

result = 0

if y == "+":
    result = (x + z)
elif y == "-":
    result = (x - z)
elif y == "*":
    result = (x * z)
elif y == "/":
    result = (x / z)
else:
    print("Expression not supported")

print(f"{result:.1f}")
