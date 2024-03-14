import sys
import csv


def main():

    if len(sys.argv) == 3:
        if is_csv(sys.argv[1]) and is_csv(sys.argv[2]):
            try:
                convert(sys.argv[1], sys.argv[2])
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")


def is_csv(filename):
    if filename.endswith(".csv"):
        return True
    return False


def convert(finput, foutput):
    data = []

    with open(finput) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    for val in data:
        full_name = val["name"].strip('"').split(", ")
        val["name"] = full_name[1]
        val["surname"] = full_name[0]

    fieldnames = ["name", "surname", "house"]

    with open(foutput, "w") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    main()
