lilly_age = int(input())
laundry_machine_price = float(input())
toy_price = int(input())

number = 0
for i in range(1, lilly_age+1, +2):
    number += 1
toys_money = toy_price * number

even_birthdays_money = 0
diff_number = 0
another_number = 0
for n in range(2, lilly_age+1, +2):
    even_birthdays_money = 10 + another_number - 1 + diff_number
    another_number = even_birthdays_money
    diff_number += 10

total = even_birthdays_money + toys_money

if total >= laundry_machine_price:
    print(f'Yes! {total-laundry_machine_price:.2f}')
else:
    print(f'No! {laundry_machine_price-total:.2f}')
