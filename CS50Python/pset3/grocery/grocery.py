grocery = {}

while True:
    try:
        item = input()
        if item == "":
              break
        item = item.upper()
        grocery[item] = grocery.get(item, 0) +1
    except EOFError:
        break

for item in sorted(grocery):
            print(grocery[item], item, sep=", ")
