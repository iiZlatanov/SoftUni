def exchange_command(current_array_state: list, splitting_index: int):
    if splitting_index >= len(current_array_state) - 1:
        print("Invalid index")
        return current_array_state
    elif splitting_index < len(current_array_state) - 1:
        first_half = current_array_state[0:splitting_index + 1]
        second_half = current_array_state[splitting_index + 1:]
        resulting_array = second_half + first_half
        return resulting_array


def max_even_or_odd_command(current_array_state: list, even_or_odd: str):
    if even_or_odd == "even":
        list_of_all_even_numbers = []
        for number in current_array_state:
            if number % 2 == 0:
                list_of_all_even_numbers.append(number)
        if len(list_of_all_even_numbers) == 0:
            return "No matches"
        else:
            max_even_number = max(list_of_all_even_numbers)
            index_counter = 0
            result_index = 0
            for number in current_array_state:
                if number == max_even_number:
                    result_index = index_counter
                index_counter += 1
            return result_index

    elif even_or_odd == "odd":
        list_of_all_odd_numbers = []
        for number in current_array_state:
            if number % 2 != 0:
                list_of_all_odd_numbers.append(number)
        if len(list_of_all_odd_numbers) == 0:
            return "No matches"
        else:
            max_odd_number = max(list_of_all_odd_numbers)
            index_counter = 0
            result_index = 0
            for number in current_array_state:
                if number == max_odd_number:
                    result_index = index_counter
                index_counter += 1
            return result_index


def min_even_or_odd_command(current_array_state: list, even_or_odd: str):
    if even_or_odd == "even":
        list_of_all_even_numbers = []
        for number in current_array_state:
            if number % 2 == 0:
                list_of_all_even_numbers.append(number)
        if len(list_of_all_even_numbers) == 0:
            return "No matches"
        else:
            min_even_number = min(list_of_all_even_numbers)
            index_counter = 0
            result_index = 0
            for number in current_array_state:
                if number == min_even_number:
                    result_index = index_counter
                index_counter += 1
            return result_index

    elif even_or_odd == "odd":
        list_of_all_odd_numbers = []
        for number in current_array_state:
            if number % 2 != 0:
                list_of_all_odd_numbers.append(number)
        if len(list_of_all_odd_numbers) == 0:
            return "No matches"
        else:
            min_odd_number = min(list_of_all_odd_numbers)
            index_counter = 0
            result_index = 0
            for number in current_array_state:
                if number == min_odd_number:
                    result_index = index_counter
                index_counter += 1
            return result_index


def first_n_of_even_or_odd(current_array_state: list, count: int, even_or_odd: str):
    if count > len(current_array_state):
        return "Invalid count"

    else:
        if even_or_odd == "even":
            list_of_even_numbers = []
            for number in current_array_state:
                if number % 2 == 0:
                    list_of_even_numbers.append(number)
            if count >= len(list_of_even_numbers):
                return list_of_even_numbers
            else:
                result_list = list_of_even_numbers[0: count]
                return result_list

        elif even_or_odd == "odd":
            list_of_odd_numbers = []
            for number in current_array_state:
                if number % 2 != 0:
                    list_of_odd_numbers.append(number)
            if count >= len(list_of_odd_numbers):
                return list_of_odd_numbers
            else:
                result_list = list_of_odd_numbers[0: count]
                return result_list


def last_n_of_even_or_odd(current_array_state: list, count: int, even_or_odd: str):
    if count > len(current_array_state):
        return "Invalid count"

    else:
        if even_or_odd == "even":
            list_of_even_numbers = []
            for number in current_array_state:
                if number % 2 == 0:
                    list_of_even_numbers.append(number)
            if count >= len(list_of_even_numbers):
                return list_of_even_numbers
            else:
                result_list = list_of_even_numbers[len(list_of_even_numbers) - count: len(list_of_even_numbers)]
                return result_list

        elif even_or_odd == "odd":
            list_of_odd_numbers = []
            for number in current_array_state:
                if number % 2 != 0:
                    list_of_odd_numbers.append(number)
            if count >= len(list_of_odd_numbers):
                return list_of_odd_numbers
            else:
                result_list = list_of_odd_numbers[len(list_of_odd_numbers) - count: len(list_of_odd_numbers)]
                return result_list


array_data = list(map(int, input().split()))
command = input()
while command != "end":
    split_command = command.split()

    if split_command[0] == "exchange":
        array_data = exchange_command(array_data, int(split_command[1]))
    elif command == "max odd" or command == "max even":
        print(max_even_or_odd_command(array_data, split_command[1]))
    elif command == "min odd" or command == "min even":
        print(min_even_or_odd_command(array_data, split_command[1]))
    elif split_command[0] == "first":
        print(first_n_of_even_or_odd(array_data, int(split_command[1]), split_command[2]))
    elif split_command[0] == "last":
        print(last_n_of_even_or_odd(array_data, int(split_command[1]), split_command[2]))

    command = input()

print(array_data)
