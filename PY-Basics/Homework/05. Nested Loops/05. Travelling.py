while True:
    line = input()
    if line == 'End':
        break
    destination = line
    minimal_budget = float(input())
    saved_money = 0
    while saved_money < minimal_budget:
        how_much_you_saved = float(input())
        saved_money += how_much_you_saved
    print(f'Going to {destination}!')