import sys

def is_python(filename):
    if filename.endswith(".py"):
        return True
    return False

def in_docstring(line):
    if 


def main():

    line_count = 0

    if len(sys.argv) == 2 and is_python(sys.argv[1]):
        try:
            with open(sys.argv[1]) as file:
                for line in file:
                    line = line.strip()
                    if line.startswith('"""') or line.startswith("#") or line == "":
                        continue
                    else:
                        line_count += 1
        except FileNotFoundError:
            sys.exit("File does not exist")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not is_python(sys.argv[1]):
        sys.exit("Not a Python file")

    print(line_count)

if __name__ == "__main__":
    main()
