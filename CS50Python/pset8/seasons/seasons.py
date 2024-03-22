from datetime import date
import inflect
import re
import sys

p = inflect.engine()


def main():

    dob = validate_dob(input("Date of birth: "))

    # Calculate delta time in minutes
    elapsed = date.today() - dob
    elapsed_minutes = int(elapsed.total_seconds() / 60)

    # Convert to words
    elapsed_words = p.number_to_words(elapsed_minutes, andword="").capitalize() + " minutes"

    print(elapsed_words)


# Validate and convert input to date
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
