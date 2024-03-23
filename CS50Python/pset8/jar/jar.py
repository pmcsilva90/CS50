class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity


    def __str__(self):
        return 🍪 * self.capacity

    def deposit(self, n):
        return self.capacity + n

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
