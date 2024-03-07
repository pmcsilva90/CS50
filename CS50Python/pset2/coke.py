due = 50

while True:
    print(f"Amount due: {due}")
    coin = int(input("Insert coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        due -= coin
        if due <= 0:
            print(f"Change owed: {due * -1}")
            break
    else:
        continue



