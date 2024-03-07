def main():
    time = input("What time is it? ")
    convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)
    return hour + (minute / 60)


if __name__ == "__main__":
    main()
