import sys

class Jar:
    def __init__(self, capacity=12, size=0):
        if capacity < 0 or capacity < size or size < 0:
            raise ValueError
        # if capacity < size:
        #     raise ValueError
        # if size < 0:
        #     raise ValueError
        self._capacity = capacity
        self._size = size

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0 or value < self._size:
            raise ValueError
        self._capacity = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value < 0 or value > self._capacity:
            raise ValueError
        self._size = value

def main():

    cap = int(input("Jar capacity: "))
    cookies = int(input("Number of cookies: "))

    pot = Jar(cap, cookies)

    print(pot)

    while True:
        action = input("Choose: deposit; withdraw; exit -> ")
        if action.lower() == "deposit":
            pot.deposit(int(input("Deposit: ")))
            print(pot)
        elif action.lower() == "withdraw":
            pot.withdraw(int(input("Withdraw: ")))
            print(pot)
        elif action.lower() == "exit":
            print(pot)
            sys.exit()
        else:
            pass


if __name__ == "__main__":
    main()
