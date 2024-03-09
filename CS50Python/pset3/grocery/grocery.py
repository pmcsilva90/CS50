grocery = {}

while True:
    try:
        item = input()
        item = item.upper()
        grocery[item] = grocery.get(item, 0) +1
    except EOFError:
        break

for item in grocery:
            print(grocery[item], item, sep=", ")
