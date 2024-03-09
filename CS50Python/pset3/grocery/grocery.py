grocery = {}

while True:
    try:
        item = input()
        input = input.upper()
        grocery[item] += 1
    except EOFError:
        for item in grocery:
            print(item, grocery[item], sep=",")
        break
