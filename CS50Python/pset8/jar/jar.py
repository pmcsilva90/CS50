class Jar:
    def __init__(self, capacity=12, cookies=0):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.size = size


    def __str__(self):
        return 🍪 * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        return self.size + n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        return self.size - n

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self.size
