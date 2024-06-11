class Person:
    def __init__(self, name: str):
        self.name = name
        self.__security_number = "123456"

    def get_security_number(self) -> str:
        return self.__security_number[4:]

    def set_security_number(self, new_value: str) -> None:
        today = "2024-01-01"
        if today > "2024-03-01":
            self.__security_number = new_value


p = Person("Test")

print(p.name)
p.name = ""
print(p.name)
print(p.get_security_number())
