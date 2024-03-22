from datetime import date
import inflect
import re
import sys

p = inflect.engine()


def main():
    # mybday = date(1990, 3, 18)
    # mybdaypl1 = date(1992, 3, 18)
    # elapsed = mybdaypl1 - mybday
    # elapsed_minutes = elapsed.total_seconds() / 60

    # print(mybday)
    # print(mybdaypl1)
    # print(elapsed_minutes)
    # print(p.number_to_words(int(elapsed_minutes), andword="").capitalize())

    dob_input = validate_dob(input("Date of birth: "))

    dob_date = date(dob_input[0], dob_input[1], dob_input[2])
    elapsed = date.today() - dob_date
    elapsed_minutes = int(elapsed.total_seconds() / 60)
    elapsed_words = p.number_to_words(elapsed_minutes, andword="").capitalize() + " minutes"
    print(elapsed_words)

def validate_dob(s):
    if matches := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", s):
        year, month, day = matches.groups()
        return int(year), int(month), int(day)
    else:
        sys.exit("Invalid date")





if __name__ == "__main__":
    main()
