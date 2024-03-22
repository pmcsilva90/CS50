from datetime import date


def main():
    mybday = date(1990, 3, 18)
    mybdaypl1 = date(1991, 3, 18)
    elapsed = mybdaypl1 - mybday

    print(mybday)
    print(mybdaypl1)
    print(elapsed.total_seconds() / 60)


if __name__ == "__main__":
    main()
