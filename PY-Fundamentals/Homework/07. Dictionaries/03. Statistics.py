data = input()
my_dict = {}

while data != "statistics":
    data_list = data.split(": ")
    if data_list[0] in my_dict:
        my_dict[data_list[0]] += int(data_list[1])
    else:
        my_dict[data_list[0]] = int(data_list[1])
    data = input()

print(my_dict)