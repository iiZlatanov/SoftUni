secret_message = input().split()
current_letter = ""
deciphering = ""

for element in secret_message:
    for each_index in element:
        if each_index.isdigit() is True:
            current_letter += each_index
    deciphering += chr(int(current_letter))
    for each_index in element:
        if each_index.isalpha() is True:
            deciphering += each_index
    deciphering += " "
    current_letter = ""

still_deciphering = deciphering.split(" ")
still_deciphering = [el for el in still_deciphering if len(el) > 1]
deciphering_done = []
word = ""

for element in still_deciphering:
    saved_index_one = element[1]
    saved_index_two = element[-1]
    counter = 0
    for each_letter in element:
        counter += 1
        if len(element) == counter:
            word += saved_index_one
        elif counter != 2:
            word += each_letter
        elif counter == 2:
            word += saved_index_two
        if len(element) == counter:
            counter = 0
    word += " "

print(word)
