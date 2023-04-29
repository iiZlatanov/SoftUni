data = input()
index = []

for i in range(len(data)):
    ch = data[i]

    if ch == "(":
        index.append(i)
    elif ch == ")":
        closing = index.pop()
        print(data[closing: i+1])
