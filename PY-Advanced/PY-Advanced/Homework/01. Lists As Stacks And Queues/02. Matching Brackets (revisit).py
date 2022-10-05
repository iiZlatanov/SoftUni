expression = input()

s = []

for i in range(len(expression)):
    character = expression[i]
    if character == "(":
        s.append(i)
    elif character == ")":
        print(expression[s[-1]:i + 1])
        s.pop()
