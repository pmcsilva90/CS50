import sys


def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not is_python(sys.argv[1]):
        sys.exit("Not a Python file")

    try:
        print(count_lines(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("File does not exist")


def is_python(filename):
    if filename.endswith(".py"):
        return True
    return False


def count_lines(pycode):
    line_count = 0

    with open(pycode) as file:
        for line in file:
            line = line.strip()
            if line.startswith("#") or line == "":
                continue
            else:
                line_count += 1

    return line_count


if __name__ == "__main__":
    main()
