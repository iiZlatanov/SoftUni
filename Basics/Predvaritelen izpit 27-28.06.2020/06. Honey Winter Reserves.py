needed_honey_to_survive_the_winter = float(input())
total = 0
flag = False

while True:
    name_of_bee = input()
    if total >= needed_honey_to_survive_the_winter:
        print(f'Well done! Honey surplus {(total - needed_honey_to_survive_the_winter):.2f}.')
        flag = True
        break
    if name_of_bee == 'Winter has come':
        if total >= needed_honey_to_survive_the_winter:
            print(f'Well done! Honey surplus {(total - needed_honey_to_survive_the_winter):.2f}.')
            flag = True
            break
        elif total < needed_honey_to_survive_the_winter:
            print(f'Hard Winter! Honey needed {(needed_honey_to_survive_the_winter - total):.2f}.')
            flag = True
            break
    for i in range(6):
        harvested_per_month = float(input())
        if harvested_per_month < 0:
            print(f'{name_of_bee} was banished for gluttony')
            break
        harvested_per_month_into_string = str(harvested_per_month)
        if harvested_per_month_into_string == 'Winter has come':
            if total >= needed_honey_to_survive_the_winter:
                print(f'Well done! Honey surplus {(total - needed_honey_to_survive_the_winter):.2f}.')
                flag = True
                break
            elif total < needed_honey_to_survive_the_winter:
                print(f'Hard Winter! Honey needed {(needed_honey_to_survive_the_winter - total):.2f}.')
                flag = True
                break
        total += harvested_per_month
        if total >= needed_honey_to_survive_the_winter:
            print(f'Well done! Honey surplus {(total - needed_honey_to_survive_the_winter):.2f}.')
            flag = True
            break
    if total < 0:
        print(f'{name_of_bee} was banished for gluttony')
    if flag:
        break