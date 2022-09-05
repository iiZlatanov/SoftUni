from collections import deque
GREEN_LIGHT_DURATION = int(input())
FREE_WINDOW_DURATION = int(input())

command = input()
cars_waiting = deque()
total_cars_that_passed_the_crossroad = 0
flag = True

while command != "END":
    if command != "green":
        cars_waiting.append(command)

    elif command == "green":
        current_green_light_duration = GREEN_LIGHT_DURATION
        while current_green_light_duration > 0 and len(cars_waiting) > 0:
            front_most_car = cars_waiting[0]
            cars_waiting.popleft()
            total_cars_that_passed_the_crossroad += 1
            if current_green_light_duration + FREE_WINDOW_DURATION < len(front_most_car): # This is the crash scenario
                crash_index = - (len(front_most_car) - (current_green_light_duration + FREE_WINDOW_DURATION))
                print(f"A crash happened!\n{front_most_car} was hit at {front_most_car[crash_index]}.")
                flag = False
                break
            current_green_light_duration -= len(front_most_car)
    if flag is False:
        break
    command = input()

if flag is True:
    print(f"Everyone is safe.\n{total_cars_that_passed_the_crossroad} total cars passed the crossroads.")
