from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


s = Stack()
print(s.is_empty())
s.push("a")
s.push("b")
s.push("c")
s.push("d")
print(s)
print(s.pop())
s.push("e")
print(s)
print(s.is_empty())
