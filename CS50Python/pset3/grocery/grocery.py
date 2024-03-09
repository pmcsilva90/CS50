grocery = {}

while True:
    try:
        item = input()
        grocery[item] =
    except KeyError:

        pass
    except EOFError:
        for item in grocery:
            print(grocery[item], item, sep=", ")
        break
