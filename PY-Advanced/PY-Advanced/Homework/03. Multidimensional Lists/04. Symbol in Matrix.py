rows_and_columns = int(input())
matrix = []
coordinates = []
row_index = 0
column_index = 0
flag = False
flag_two = False

for _ in range(rows_and_columns):
    row_symbols = input()
    row = []
    for symbol in row_symbols:
        row.append(symbol)
    matrix.append(row)

searched_symbol = input()

for lists in matrix:
    for characters in lists:
        if characters == searched_symbol:
            flag_two = True

if flag_two is False:
    print(f"{searched_symbol} does not occur in the matrix")
else:
    for each_list in matrix:
        for each_character in each_list:
            if each_character == searched_symbol:
                flag = True
                break
            else:
                column_index += 1
                if column_index == rows_and_columns:
                    column_index = 0
                    row_index += 1
        if flag is True:
            break
    result_tuple = (row_index, column_index)
    print(result_tuple)
