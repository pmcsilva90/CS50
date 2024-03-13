import sys

line_count = 0

with open(argv[1]) as file:
    for line in file:
        line.strip()
        if line.startswith('"""') or line.startswith("#"):
            continue
        else:
            line_count += 1

