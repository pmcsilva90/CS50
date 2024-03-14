import sys
import csv


def main():

    if len(sys.argv) == 3:
        if is_csv(sys.argv[1]):
            try:
                ...
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

def convert(finput, foutput)
    data = []

    with open(finput) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.replace(row('"', ''))
            data.append({"surname": row[0], "name": row[1], "house": row[2]})

    if is_csv(foutput):
        with open(foutput, "a") as file:
            writer = csv.DictWriter(file)
            writer.writerow("key")
    else:
        sys.exit("Output must be CSV file")




if __name__ == "__main__":
    main()
