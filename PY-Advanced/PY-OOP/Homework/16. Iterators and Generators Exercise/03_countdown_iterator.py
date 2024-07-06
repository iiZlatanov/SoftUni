class countdown_iterator:
    def __init__(self, count):
        self.count = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise StopIteration

        return self.count


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

print("--------")

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
