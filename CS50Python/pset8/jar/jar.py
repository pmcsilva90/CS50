class Jar:
    def __init__(self, , capacity=12cookies=0):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.cookies = cookies


    def __str__(self):
        return 🍪 * self.cookies

    def deposit(self, n):
        if self.cookies + n > self.capacity:
            raise ValueError
        return self.cookies + n

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
