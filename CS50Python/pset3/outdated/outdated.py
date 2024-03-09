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

month, day, year = date.split("/")

month = int(month)
day = int(day)
year = int(year)

print(year, month, day)
