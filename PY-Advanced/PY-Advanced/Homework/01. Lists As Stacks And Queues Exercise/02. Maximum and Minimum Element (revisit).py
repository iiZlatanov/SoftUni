number_of_iterations = int(input())
result = []
end_result = []

for _ in range(number_of_iterations):
    data = input()
    if len(data) == 1:
        command = int(data)
        if command == 2:
            if len(result) > 0:
                result.pop()
        elif command == 3:
            print(max(result))
        elif command == 4:
            print(min(result))
    else:
        command_and_number = data.split()
        result.append(int(command_and_number[1]))

while len(result) > 0:
    element = result.pop()
    end_result.append(element)

print(", ".join(list(map(str, end_result))))
