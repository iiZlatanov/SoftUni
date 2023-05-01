NUMBER_OF_INQUIRIES = int(input())
stack = []

for _ in range(NUMBER_OF_INQUIRIES):
    data = input().split()
    if data[0] == "1":
        stack.append(int(data[1]))
    elif data[0] == "2":
        if len(stack) > 0:
            stack.pop()
    elif data[0] == "3":
        print(max(stack))
    else:
        print(min(stack))

print(", ".join(list(map(str, reversed(stack)))))
