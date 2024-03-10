import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break

names = p.join((names), final_sep=",")

print("Adieu, adieu, to " + names)
