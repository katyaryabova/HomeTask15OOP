class Counter:
    current = 0

    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end

    def increase(self):
        if self.current < self.end:
            self.current += 1
            return self.current
        else:
            return 'Out of range'


my_count = Counter(start=0, end=3)
print(my_count.increase())
print(my_count.increase())
print(my_count.increase())
print(my_count.increase())  # 'Out of range'
