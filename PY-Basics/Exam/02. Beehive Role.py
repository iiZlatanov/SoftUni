intellect = int(input())
strength = int(input())
sex = input()

if intellect >= 80 and strength >= 80 and sex == 'female':
    print('Queen Bee')
elif intellect >= 80:
    print('Repairing Bee')
elif intellect >= 60:
    print('Cleaning Bee')
elif strength >= 80 and sex == 'male':
    print('Drone Bee')
elif strength >= 60:
    print('Guard Bee')
else:
    print('Worker Bee')