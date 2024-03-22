from datetime import date


def main():
    mybday = date(1990, 3, 18)
    tday = date.today()
    elapsed = tday - mybday

    print(mybday)
    print(tday)
    print(elapsed)








if __name__ == "__main__":
    main()
