class reverse_iter:
    pass

    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.start_idx = len(iterable) - 1
        self.end_idx = 0
        self.current_idx = self.start_idx + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_idx -= 1

        if self.current_idx < self.end_idx:
            raise StopIteration()

        return self.iterable[self.current_idx]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
