kids = input().split()
NUMBER_OF_JUMPS = int(input())
index = -1

while len(kids) > 1:
    for n in range(NUMBER_OF_JUMPS):
        index += 1
        if index > len(kids) - 1:
            index = 0
    print(f"Removed {kids[index]}")
    kids.pop(index)
    index -= 1

print(f"Last is {kids[0]}")
