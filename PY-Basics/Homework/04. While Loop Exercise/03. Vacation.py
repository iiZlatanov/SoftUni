required_money_for_vacation = float(input())
current_money_owned = float(input())
days = 0
spending_counter = 0

while True:
    spend_or_save = input()
    number = float(input())
    days += 1
    if spend_or_save == 'save':
        current_money_owned += number
        spending_counter = 0
    elif spend_or_save == 'spend':
        current_money_owned -= number
        spending_counter += 1
    if current_money_owned >= required_money_for_vacation:
        print(f'You saved the money for {days} days.')
        break
    if spending_counter >= 5:
        print("You can't save the money.")
        print(days)
        break
    if current_money_owned < 0:
        current_money_owned = 0