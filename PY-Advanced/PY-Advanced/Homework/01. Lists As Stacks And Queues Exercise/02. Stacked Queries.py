stack = []

for _ in range(int(input())):
    data = [int(x) for x in input().split()]
    command = data[0]
    if command == 1:
        stack.append(data[1])
    elif command == 2 and len(stack) > 0:
        stack.pop()
    elif command == 3 and len(stack) > 0:
        print(max(stack))
    elif command == 4 and len(stack) > 0:
        print(min(stack))

result = []
for el in reversed(stack):
    result.append(el)
print(", ".join(str(x) for x in result))
