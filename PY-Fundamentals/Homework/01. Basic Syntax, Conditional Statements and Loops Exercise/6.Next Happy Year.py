year = int(input())
year += 1
length_of_str_of_year = len(str(year))
length_of_set_of_str_of_year = len(set(str(year)))

while length_of_str_of_year != length_of_set_of_str_of_year:
    year += 1
    length_of_str_of_year = len(str(year))
    length_of_set_of_str_of_year = len(set(str(year)))
    if length_of_str_of_year == length_of_set_of_str_of_year:
        break

print(year)