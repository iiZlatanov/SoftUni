from typing import Union


class Account:
    def __init__(self, id: int, balance: int, pin: int) -> None:
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin: int) -> Union[str, int]:
        if pin != self.__pin:
            return "Wrong pin"

        return self.__id

    def change_pin(self, old_pin: int, new_pin: int) -> str:
        if old_pin != self.__pin:
            return "Wrong pin"

        self.__pin = new_pin
        return "Pin changed"


account = Account(8827312, 100, 3421)

print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))

# Wrong pin
# 8827312
# 100
# Wrong pin
# Pin changed
