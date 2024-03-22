from datetime import date
import inflect
import re
import sys

p = inflect.engine()


def main():

    dob_input = validate_dob(input("Date of birth: "))

    # Convert to date format
    dob_date = date(dob_input[0], dob_input[1], dob_input[2])

    # Calculate delta time in minutes
    elapsed = date.today() - dob_date
    elapsed_minutes = int(elapsed.total_seconds() / 60)

    # Convert to words
    elapsed_words = p.number_to_words(elapsed_minutes, andword="").capitalize() + " minutes"

    print(elapsed_words)

def validate_dob(s):
    if matches := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", s):
        year, month, day = map(int, matches.groups())
        try:
            d = date(year, month, day)
            return d
        except ValueError:
            sys.exit("Invalid date")
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
