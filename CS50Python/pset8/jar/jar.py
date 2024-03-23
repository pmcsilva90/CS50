class Jar:
    def __init__(self, capacity=12, size=0):
        if capacity < 0:
            raise ValueError
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

    pot = Jar()

    print(pot)

    pot.deposit(int(input("Deposit: ")))

    print(pot)

    pot.withdraw(int(input("Withdraw: ")))

    print(pot)

    pot.capacity = 15

    print(pot)

    pot.size = 10

    print(pot)

if __name__ == "__main__":
    main()
