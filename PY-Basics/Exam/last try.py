honey_needed = float(input())
total = 0
flag = False

while True:
    name_of_the_bee = input()
    if name_of_the_bee != 'Winter has come':
        for i in range(6):
            harvested = float(input())
            string_of_harvested = str(harvested)
            if string_of_harvested == 'Winter has come':
                if total >= honey_needed:
                    print(f'Well done! Honey surplus {(total - honey_needed):.2f}.')
                    flag = True
                    break
                elif total < honey_needed:
                    print(f'Hard Winter! Honey needed {(honey_needed - total):.2f}.')
                    flag = True
                    break
            total += harvested
            if total >= honey_needed:
                print(f'Well done! Honey surplus {(total - honey_needed):.2f}.')
                flag = True
                break
        if total < 0:
            print(f'{name_of_the_bee} was banished for gluttony.')
        if flag:
            break
    elif name_of_the_bee == 'Winter has come':
        if total >= honey_needed:
            print(f'Well done! Honey surplus {(total - honey_needed):.2f}.')
            break
        elif total < honey_needed:
            print(f'Hard Winter! Honey needed {(honey_needed - total):.2f}.')
            break

