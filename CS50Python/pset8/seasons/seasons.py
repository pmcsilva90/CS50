from datetime import date
import inflect

p = inflect.engine()


def main():
    mybday = date(1990, 3, 18)
    mybdaypl1 = date(1992, 3, 18)
    elapsed = mybdaypl1 - mybday
    elapsed_minutes = elapsed.total_seconds() / 60

    print(mybday)
    print(mybdaypl1)
    print(elapsed_minutes)
    print(p.number_to_words(int(elapsed_minutes), andword=""))


if __name__ == "__main__":
    main()
