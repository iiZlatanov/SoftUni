from collections import deque

kids = deque(input().split())
JUMPS = int(input())

while len(kids) > 1:
    for i in range(JUMPS - 1):
        kids.append(kids.popleft())
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids[0]}")
