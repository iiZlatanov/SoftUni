n = int(input())
even = []
odd = []
negative = []
positive = []

for i in range(n):
    number = int(input())
    if number == 0:
        even.append(number)
        positive.append(number)
    elif number > 0:
        positive.append(number)
    elif number < 0:
        negative.append(number)
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

command = input()

if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "negative":
    print(negative)
elif command == "positive":
    print(positive)