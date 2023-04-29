#	Premiere – премиерна прожекция, на цена 12.00 лева;
#	Normal – стандартна прожекция, на цена 7.50 лева;
#	Discount – прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.



projection_type = input()
rows = int(input())
columns = int(input())

multiply = rows * columns
total = 0

if projection_type == 'Premiere':
    total = multiply * 12.00
    print(f'{total:.2f} leva')
elif projection_type == 'Normal':
    total = multiply * 7.50
    print(f'{total:.2f} leva')
elif projection_type == 'Discount':
    total = multiply * 5.00
    print(f'{total:.2f} leva')