number_of_bees = int(input())
health_of_bear = int(input())
attack_of_bear = int(input())


while True:
    number_of_bees -= attack_of_bear
    bee_attack = number_of_bees * 5
    health_of_bear -= bee_attack
    if number_of_bees < 100:
        if number_of_bees < 0:
            number_of_bees = 0
        print(f'The bear stole the honey! Bees left {number_of_bees}.')
        break
    elif health_of_bear <= 0:
        print(f'Beehive won! Bees left {number_of_bees}.')
        break