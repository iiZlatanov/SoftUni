from collections import deque

data = deque(str(x) for x in input())

possibilities = ["()", "{}", "[]"]
flag = True

if len(data) % 2 == 1:
    data = []
    flag = False

while data:
    a = data.popleft()
    b = data.pop()
    c = a + b
    if c not in possibilities:
        flag = False
        break

if flag is True:
    print("YES")
elif flag is False:
    print("NO")
