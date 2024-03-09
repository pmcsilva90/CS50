months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

date = input("Date: ")
date = date.strip()

try:
    month, day, year = date.split("/")
    month = month(int)
except ValueError:
    month, day, year = date.split(" ")
    if month in months:
        month = int()

month = int(month)
day = int(day)
year = int(year)

print(year, month, day)
