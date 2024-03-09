grocery = {}

while True:
    try:
        item = input()
        item = item.upper()
        if grocery[item] > 0:
            if item in grocery:
                grocery[item] += 1
        else:
            grocery[item] = 0
    except KeyError:
        pass
    except EOFError:
        for item in grocery:
            print(grocery[item], item, sep=", ")
        break
