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
        if 0 < month <= 12 and 0 < day <= 31:
            break
    except ValueError:
        try:
            month, day, year = date.split(" ")
            month = month.capitalize()
            if month in months and 0 < day <= 31:
                month = months.index(month) + 1
                break
            else:
                pass
        except ValueError:
            pass

print(year, month, day, sep="-")
