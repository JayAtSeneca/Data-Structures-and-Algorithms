class UpCounter:
    def __init__(self, size = 1):
        self.size = size
        self.counter = 0
    def count(self):
        return self.counter
    def update(self):
        self.counter += self.size
class DownCounter(UpCounter):
    def __init__(self, size=1):
        super().__init__(size)
    def update(self):
        self.counter -= self.size

counter=DownCounter(3)
counter.update()
counter.update()
counter.update()
print(counter.count(),-9)
counter.update()
counter.update()
print(counter.count(),-15)