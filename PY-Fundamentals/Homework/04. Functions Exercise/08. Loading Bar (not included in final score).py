number = int(input())

if number == 100:
    print("100% Complete!\n[%%%%%%%%%%]")
else:
    actual_string = f"{number}% ["
    counter = number / 10
    for i in range(1, int(counter + 1)):
        actual_string += "%"
    while True:
        if len(actual_string) < 15:
            actual_string += "."
        elif len(actual_string) == 15:
            actual_string += "]"
            break
    print(actual_string)
    print("Still loading...")