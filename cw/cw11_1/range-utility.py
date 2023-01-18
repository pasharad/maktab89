class Range:
    
    def __init__(self, end: int, start=0, step=1) -> None:
        self.start = start
        self.end = end
        self.step = step
        if start > end:
            self.start, self.end = self.end, self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            x = self.start
            self.start += self.step
            return x
        else:
            raise StopIteration


my_list = Range(10, 1, 2)
x = iter(my_list)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))



