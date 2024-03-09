grocery = {}

while True:
    try:
        item = input()
        item = item.upper()
        grocery[item] = 1
        if grocery[item] > 0:
            grocery[item] += 1
    except EOFError:
        for item in grocery:
            print(grocery[item], item, sep=", ")
        break
