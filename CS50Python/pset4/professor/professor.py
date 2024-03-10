import random


def main():
    ...


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(3):
                return level
        except KeyError:
            pass


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
