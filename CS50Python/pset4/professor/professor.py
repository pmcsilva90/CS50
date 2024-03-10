import random


def main():
    n = get_level()

    for _ in range(10):

        x = generate_integer(n)
        y = generate_integer(n)
        ans = int(input(f"{x} + {y} = "))
        if ans != x + y:
            


    i = generate_integer(n)

    print(i)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level <= 3:
                return level
        except (KeyError, ValueError):
            pass


def generate_integer(level):
    return random.randint(0, ((10 ** level) - 1))


if __name__ == "__main__":
    main()
