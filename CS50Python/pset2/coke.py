due = 50

while True:
    print("Amount due: " + due)
    coin = int(input("Insert coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        due -= coin
        


