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

while True:
    try:
        date = input("Date: ")
        date = date.strip()
        month, day, year = date.split("/")
        break
    except ValueError:
        month, day, year = date.split(" ")
        if month in months:
            month = months.index(month)
            break
        else:
            pass

month = int(month)
day = int(day)
year = int(year)

print(year, month, day)
