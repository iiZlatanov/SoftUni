result, *data = input().split()
result = int(result)
idx = 1

while idx < len(data):
    element = data[idx]

    if element in "+-*/":
        for x in data[0:idx]:
            if element == '+':
                result += int(x)
            elif element == '-':
                result -= int(x)
            elif element == '*':
                result *= int(x)
            else:
                result = result // int(x)
        data = data[(idx+1)::]
        idx = -1
    idx += 1

print(result)
