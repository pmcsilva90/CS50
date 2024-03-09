grocery = {}

while True:
    try:
        item = input()
        item = item.upper()
        if item in grocery:
            grocery[item] += 1
    except EOFError:
        for item in grocery:
            print(grocery[item], item, sep=",")
        break
