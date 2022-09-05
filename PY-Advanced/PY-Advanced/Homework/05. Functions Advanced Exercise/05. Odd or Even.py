command = input()
numbers = [int(el) for el in input().split()]

if command == "Odd":
    print(sum(filter(lambda x: x % 2 != 0, numbers)) * len(numbers))
elif command == "Even":
    print(sum(filter(lambda x: x % 2 == 0, numbers)) * len(numbers))
