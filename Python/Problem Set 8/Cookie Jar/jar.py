class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Deposit amount must be a non-negative integer")
        if self.size + n > self.capacity:
            raise ValueError("Exceeds jar capacity")
        self.size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Withdrawal amount must be a non-negative integer")
        if self.size < n:
            raise ValueError("Not enough cookies in the jar")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size
