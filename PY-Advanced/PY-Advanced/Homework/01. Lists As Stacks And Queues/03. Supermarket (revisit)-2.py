from collections import deque

names_deque = deque()
COMMAND_END = "End"
COMMAND_PAID = "Paid"

while True:
    command = input()

    if command == COMMAND_END:
        print(f"{len(names_deque)} people remaining.")
        break
    elif command == COMMAND_PAID:
        while len(names_deque) > 0:
            print(names_deque.popleft())
    else:
        names_deque.append(command)

