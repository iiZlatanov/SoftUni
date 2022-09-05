data = list(input())

reversed_word = []

while len(data) > 0:
    reversed_word.append(data[-1])
    data.pop()

print("".join(reversed_word))
