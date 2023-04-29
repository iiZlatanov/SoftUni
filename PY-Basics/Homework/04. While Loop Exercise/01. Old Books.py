searched_book_name = input()
number_of_searches = 0

while True:
    book_name = input()
    number_of_searches += 1
    if searched_book_name == book_name:
        number_of_searches -= 1
        print(f'You checked {number_of_searches} books and found it.')
        break
    if book_name == 'No More Books':
        number_of_searches -= 1
        print('The book you search is not here!')
        print(f'You checked {number_of_searches} books.')
        break