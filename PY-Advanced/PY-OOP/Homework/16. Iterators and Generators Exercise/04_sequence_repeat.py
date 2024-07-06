class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration()
        self.number -= 1

        self.idx += 1
        if self.idx >= len(self.sequence):
            self.idx = 0

        return self.sequence[self.idx]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

print("--------")

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
