word = input()
number_of_reps = int(input())


def repeat_string(string, rep):
    result = string * rep
    return result


print(repeat_string(word, number_of_reps))