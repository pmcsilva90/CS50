grocery = {}

while True:
    try:
        item = input()
        input = input.upper()
    except EOFError:
        print()
        break
