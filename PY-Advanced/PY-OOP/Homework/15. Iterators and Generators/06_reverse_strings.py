from collections import deque


def reverse_text(text):
    reversed_data = deque(reversed(text))

    while reversed_data:
        yield reversed_data.popleft()


for char in reverse_text("step"):
    print(char, end='')
