version = list(map(int, input().split(".")))
index = -1

if version[-1] != 9:
    version[-1] += 1
    print(".".join(map(str, version)))

elif version[-1] == 9:
    for element in version[::-1]:
        if element == 9:
            version[index] = 0
            version[index - 1] += 1
        index -= 1
    print(".".join(map(str, version)))
