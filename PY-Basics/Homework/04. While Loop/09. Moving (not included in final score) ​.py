wide = int(input())
long = int(input())
height = int(input())

room_total_space = wide * long * height
boxes_total = 0

while True:
    numbers_or_done = input()
    if numbers_or_done == 'Done':
        print(f'{room_total_space - boxes_total} Cubic meters left.')
        break
    numbers = int(numbers_or_done)
    boxes_total += numbers
    if boxes_total > room_total_space:
        print(f'No more free space! You need {boxes_total - room_total_space} Cubic meters more.')
        break