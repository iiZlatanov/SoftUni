def ascii_in_betweens(first_character: str or int, second_character: str or int):
    result = []
    for number in range(ord(first_character) + 1, ord(second_character)):
        result.append(chr(number))
    return result


print(" ".join(ascii_in_betweens(input(), input())))
