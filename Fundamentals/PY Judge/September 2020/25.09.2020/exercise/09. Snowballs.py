number_of_snowballs = int(input())

best_snowball = 0

for snowball in range(1, number_of_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    new_snowball = (snowball_snow / snowball_time) ** snowball_quality
    if new_snowball > best_snowball:
        best_snowball = new_snowball
        best_snowball_snow = snowball_snow
        best_snowball_time = snowball_time
        best_snowball_quality = snowball_quality

print(f"{best_snowball_snow} : {best_snowball_time} = {int(best_snowball)} ({best_snowball_quality})")