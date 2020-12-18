puzzle = 2.60
talking_doll = 3
teddy_bear = 4.10
minion = 8.20
truck = 2

vacation_price = float(input())
number_of_puzzles = int(input())
number_of_talking_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

money_earned = (puzzle * number_of_puzzles) + (talking_doll * number_of_talking_dolls) + (teddy_bear * number_of_teddy_bears) + (minion * number_of_minions) + (truck * number_of_trucks)

if number_of_trucks + number_of_minions + number_of_teddy_bears + number_of_talking_dolls + number_of_puzzles >= 50:
    money_earned -= money_earned * 0.25

money_earned -= money_earned * 0.1
final_money_after_vacation_price = money_earned - vacation_price
final_money_after_vacation_price = abs(final_money_after_vacation_price)
if money_earned >= vacation_price:
    print(f'Yes! {final_money_after_vacation_price:.2f} lv left.')
else: print(f'Not enough money! {final_money_after_vacation_price:.2f} lv needed.')