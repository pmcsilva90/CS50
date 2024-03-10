import random


def main():
    n = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        tries = 0

        while True:
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans != x + y:
                    print("EEE")
                    tries += 1
                    if tries == 3:
                        print(f"{x} + {y} = {x + y}")
                        break
                elif ans == x + y:
                    score += 1
                    break
            except ValueError:
                print("Invalid input")
                pass
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level <= 3:
                return level
            else:
                raise ValueError
        except (KeyError, ValueError):
            pass


def generate_integer(level):
    if level == 1
    return random.randint((10 ** (level - 1)), ((10 ** level) - 1))


if __name__ == "__main__":
    main()
