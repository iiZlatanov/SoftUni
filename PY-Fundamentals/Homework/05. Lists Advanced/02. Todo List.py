to_do_notes = input()
actual_list = [0 for _ in range(10)]
real_list = []

while to_do_notes != 'End':
    data = to_do_notes.split("-")
    number = (int(data[0])) - 1
    actual_list.insert(number, data[1])
    to_do_notes = input()

for el in actual_list:
    if el != 0:
        real_list.append(el)
print(real_list)
