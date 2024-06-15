from math import floor
from typing import TypeVar, Type, Union

T = TypeVar("T", bound='TrivialClass')


class Integer:
    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls: Type[T], value: float) -> Union[str, T]:
        if not isinstance(value, float):
            return "value is not a float"
        return cls(floor(value))

    @classmethod
    def from_roman(cls: Type[T], value: str) -> T:
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(value)):
            if i > 0 and rom_val[value[i]] > rom_val[value[i - 1]]:
                int_val += rom_val[value[i]] - 2 * rom_val[value[i - 1]]
            else:
                int_val += rom_val[value[i]]

        return cls(int_val)

    @classmethod
    def from_string(cls: Type[T], value: str) -> Union[str, T]:
        if not isinstance(value, str):
            return "wrong type"
        try:
            number = int(value)
            return cls(number)
        except ValueError:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
