import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) (to|-) (\d{1,2}):?(\d{2})? (AM|PM)", s)
    print(matches.groups())
    valid_time = False

    for n in range(1, len(matches.groups())):
        print(type(matches.groups(n)))

    list = []

    for n in range(1, len(matches.groups())):
        list.append(matches.groups(n))
        print(matches.groups(n))

    for n in list:
        print(n, type(n))

    return "done"

    #if (0 < start_h < 13) and (0 < end_h < 13) and (0 <= start_m < 60) and (0 <= end_m < 60):
        #valid_time = True
    #if to != "to":
        #sys.exit("to error")
    #if start_ampm == "PM":
        #start_h += 12
    #if end_ampm == "PM":
        #end_h += 12

    #if valid_time:
        #return f"{start_h}:{start_m} to {end_h}:{end_m}"


if __name__ == "__main__":
    main()
