from collections import deque

programmers_times = deque(int(x) for x in input().split())
tasks = [int(x) for x in input().split()]

duckies_given = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while tasks:
    result = programmers_times[0] * tasks[-1]
    if result > 240:
        tasks[-1] -= 2
        programmers_times.append(programmers_times.popleft())
    else:
        programmers_times.popleft()
        tasks.pop()
        if 0 <= result <= 60:
            duckies_given["Darth Vader Ducky"] += 1
        elif 61 <= result <= 120:
            duckies_given["Thor Ducky"] += 1
        elif 121 <= result <= 180:
            duckies_given["Big Blue Rubber Ducky"] += 1
        elif 181 <= result <= 240:
            duckies_given["Small Yellow Rubber Ducky"] += 1

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key,value in duckies_given.items():
    print(f"{key}: {value}")
