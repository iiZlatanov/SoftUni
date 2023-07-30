input_string = input()

while True:
    command = input()
    if command == "Finish":
        break

    data = command.split()
    if data[0] == "Replace":
        input_string = input_string.replace(data[1], data[2])
        print(input_string)

    elif data[0] == "Make":
        if data[1] == "Upper":
            input_string = input_string.upper()
        elif data[1] == "Lower":
            input_string = input_string.lower()
        print(input_string)

    elif data[0] == "Check":
        if data[1] in input_string:
            print(f"Message contains {data[1]}")
        else:
            print(f"Message doesn't contain {data[1]}")

    elif data[0] == "Sum":
        index_one = int(data[1])
        index_two = int(data[2])
        if index_one < 0 or index_two < 0 or index_one > len(input_string) or index_two > len(input_string):
            print("Invalid indices!")
        else:
            total = 0
            substring = input_string[index_one : index_two + 1]
            for ch in substring:
                total += ord(ch)
            print(total)

    elif data[0] == "Cut":
        index_one = int(data[1])
        index_two = int(data[2])
        if index_one < 0 or index_two < 0 or index_one > len(input_string) or index_two > len(input_string):
            print("Invalid indices!")
        else:
            substring = input_string[index_one : index_two + 1]
            input_string = input_string.replace(substring, "")
            print(input_string)
