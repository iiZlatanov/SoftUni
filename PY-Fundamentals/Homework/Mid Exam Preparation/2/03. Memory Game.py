sequence = input().split()
command = input()
number_of_moves = 0
flag = True

while command != "end":
    if len(sequence) == 0:
        flag = False
        print(f"You have won in {number_of_moves} turns!")
        break
    number_of_moves += 1
    indexes = list(map(int, command.split()))
    if indexes[0] == indexes[1] or indexes[0] >= len(sequence) or indexes[1] >= len(sequence) or indexes[0] < 0 or \
            indexes[1] < 0:
        if len(sequence) > 2:
            print("Invalid input! Adding additional elements to the board")
            sequence.insert(len(sequence) // 2, f"-{number_of_moves}a")
            sequence.insert(len(sequence) // 2, f"-{number_of_moves}a")
        elif len(sequence) == 2:
            print("Invalid input! Adding additional elements to the board")
            sequence.insert(1, f"-{number_of_moves}a")
            sequence.insert(1, f"-{number_of_moves}a")
    elif sequence[indexes[0]] == sequence[indexes[1]]:
        if indexes[0] > indexes[1]:
            print(f"Congrats! You have found matching elements - {sequence[indexes[0]]}!")
            sequence.pop(indexes[0])
            sequence.pop(indexes[1])
        elif indexes[1] > indexes[0]:
            print(f"Congrats! You have found matching elements - {sequence[indexes[0]]}!")
            sequence.pop(indexes[1])
            sequence.pop(indexes[0])
    elif sequence[indexes[0]] != sequence[indexes[1]]:
        print("Try again!")
    if len(sequence) == 0:
        flag = False
        print(f"You have won in {number_of_moves} turns!")
        break

    command = input()

if flag is True:
    print(f"Sorry you lose :(\n{' '.join(sequence)}")
