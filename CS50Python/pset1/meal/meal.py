def main():
    time = input("What time is it? ")

    



def convert(time):
    hour, minute = time.split(":")
    return hour + (minute / 60)



if __name__ == "__main__":
    main()
