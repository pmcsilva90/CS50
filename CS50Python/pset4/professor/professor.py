import random


def main():
    n = get_level()

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
    return random.randint(0, ((10 * n) - 1))


if __name__ == "__main__":
    main()
