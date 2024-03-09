grocery = {}

while True:
    try:
        item = input()
        item = item.upper()
        grocery
    except KeyError:

        pass
    except EOFError:
        for item in grocery:
            print(grocery[item], item, sep=", ")
        break
