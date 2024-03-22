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

    dob = input("Date of birth: ")

def validate_dob(s):
    if matches := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", s):
        year, month, day = matches.groups()
        return int(year), int(month), int(day)
    else:
        sys.exit("Invalid date")





if __name__ == "__main__":
    main()
