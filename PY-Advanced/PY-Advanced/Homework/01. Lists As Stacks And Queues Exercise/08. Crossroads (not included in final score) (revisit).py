from collections import deque

GREEN_LIGHT_DURATION = int(input())
FREE_WINDOW_DURATION = int(input())
cars_in_queue = deque()
successfully_passed_cars_counter = 0
flag = True

while True:
    command = input()
    if command == "END":
        break
    if command != "green":
        cars_in_queue.append(command)
    else:
        current_green_light_duration = GREEN_LIGHT_DURATION
        while current_green_light_duration > 0 and current_green_light_duration > FREE_WINDOW_DURATION:
            current_car = cars_in_queue.popleft()
            if len(current_car) <= current_green_light_duration:
                current_green_light_duration -= len(current_car)
                successfully_passed_cars_counter += 1
            else:
                print(f"A crash happened!\n{current_car} was hit at.")
                flag = False
                break


if flag:
    print(f"Everyone is safe.\n{successfully_passed_cars_counter} total cars passed the crossroads.")
