total_tickets_sold = 0
sold_student_count = 0
sold_standard_count = 0
sold_kid_count = 0
flag = False

while True:
    name_of_movie = input()
    total_tickets_sold_for_current_movie = 0
    sold_student_count_for_current_movie = 0
    sold_kid_count_for_current_movie = 0
    sold_standard_count_for_current_movie = 0
    free_seats_number = int(input())
    bought_seats = 0
    if flag:
        break
    while free_seats_number >= bought_seats:
        type_of_ticket_or_end = input()
        if type_of_ticket_or_end == 'student':
            total_tickets_sold_for_current_movie += 1
            sold_student_count_for_current_movie += 1
            sold_student_count += 1
            bought_seats += 1
            total_tickets_sold += 1
        if type_of_ticket_or_end == 'kid':
            total_tickets_sold_for_current_movie += 1
            sold_kid_count_for_current_movie += 1
            sold_kid_count += 1
            bought_seats += 1
            total_tickets_sold += 1
        if type_of_ticket_or_end == 'standard':
            total_tickets_sold_for_current_movie += 1
            sold_standard_count_for_current_movie += 1
            sold_standard_count += 1
            bought_seats += 1
            total_tickets_sold += 1
        if type_of_ticket_or_end == 'End':
            percentage = bought_seats / free_seats_number * 100
            print(f'{name_of_movie} - {percentage:.2f}% full')
            break
        if type_of_ticket_or_end == 'Finish':
            percentage = bought_seats / free_seats_number * 100
            print(f'{name_of_movie} - {percentage:.2f}% full')
            print(f'Total tickets: {total_tickets_sold}')
            print(f'{(sold_student_count_for_current_movie / total_tickets_sold_for_current_movie * 100):.2f}% student tickets.')
            print(f'{(sold_standard_count_for_current_movie / total_tickets_sold_for_current_movie * 100):.2f}% standard tickets.')
            print(f'{(sold_kid_count_for_current_movie / total_tickets_sold_for_current_movie * 100):.2f}% kids tickets.')
            flag = True
            break