steps_total = 0

while True:
    going_home_or_not = input()
    if going_home_or_not == 'Going home':
        last_steps = int(input())
        steps_total += last_steps
        if steps_total >= 10000:
            print('Goal reached! Good job!')
            print(f'{steps_total - 10000} steps over the goal!')
        else:
            print(f'{10000 - steps_total} more steps to reach goal.')
        break
    number_of_steps = int(going_home_or_not)
    steps_total += number_of_steps
    if steps_total >= 10000:
        print('Goal reached! Good job!')
        print(f'{steps_total - 10000} steps over the goal!')
        break

