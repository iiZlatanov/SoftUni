start = int(input())
end = int(input())
magic_number = int(input())

combo_count = 0
integer = 0
flag = False

for first_number in range(start, end + 1):
    for second_number in range(start, end + 1):
        combo_count += 1
        if first_number + second_number == magic_number:
            print(f'Combination N:{combo_count} ({first_number} + {second_number} = {magic_number})')
            flag = True
            break
    if flag:
        break


if not flag:
    print(f"{combo_count} combinations - neither equals {magic_number}")