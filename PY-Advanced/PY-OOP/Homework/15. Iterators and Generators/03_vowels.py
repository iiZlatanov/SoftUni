class vowels:
    pass

    def __init__(self, string) -> None:
        self.string = string
        self.current_idx = -1
        self.end_idx = len(string) - 1
        self.all_vowels = ['a', 'e', 'i', 'o', 'u', "y"]

    def __iter__(self):
        return self

    def __next__(self) -> str:
        self.current_idx += 1
        if self.current_idx > self.end_idx:
            raise StopIteration()
        current_element = self.string[self.current_idx]
        if current_element.lower() in self.all_vowels:
            return current_element
        return self.__next__()


my_string = vowels ('Abcedifuty0o')
for char in my_string:
    print (char)