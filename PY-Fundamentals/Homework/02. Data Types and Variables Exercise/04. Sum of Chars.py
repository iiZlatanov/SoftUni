number = int(input())
ascii_total = 0

for i in range(1, number + 1):
    number_input = input()
    current_number = ord(number_input)
    ascii_total += current_number

print(f"The sum equals: {ascii_total}")