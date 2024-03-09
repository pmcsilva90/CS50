grocery = {}

while True:
    try:
        item = input()
        input = input.upper()
        grocery[item] += 1
    except EOFError:
        print()
        break
