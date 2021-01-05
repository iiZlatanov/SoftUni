list_of_numbers = list(map(int, input().split(", ")))
current_boundary = 10
current_list = []

while len(list(map(str, list_of_numbers))) != 0:
    index = 0
    for element in list_of_numbers:
        if element <= current_boundary:
            if element == list_of_numbers[-1]:
                current_list.append(element)
                list_of_numbers.pop(index)
                print(f"Group of {current_boundary}'s: {current_list}")
                current_list = []
                index = 0
                break
            current_list.append(element)
            list_of_numbers.pop(index)
            current_boundary -= 10
            break
        if element == list_of_numbers[-1]:
            print(f"Group of {current_boundary}'s: {current_list}")
            current_list = []
            index = 0
            break
        index += 1
    current_boundary += 10
