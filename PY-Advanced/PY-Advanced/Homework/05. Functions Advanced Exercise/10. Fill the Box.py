from collections import deque

def fill_the_box(height, length, width, *args):
    cube_space = height * length * width
    all_commands = deque(args)
    result = ""

    while True:
        if all_commands:
            command = all_commands.popleft()
            if command == "Finish":
                result = f"There is free space in the box. You could put {cube_space} more cubes."
                break
            else:
                cube_space -= command
                if cube_space < 0:
                    rest_of_cubes = abs(cube_space) + sum([el for el in all_commands if str(el).isdigit()])
                    result = f"No more free space! You have {rest_of_cubes} more cubes."
                    break
        else:
            break

    return result


print(fill_the_box(2, 8,
2, 2, 1, 7, 3, 1, 5,
"Finish"))
# There is free space in the box. You could put 13 more cubes.

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
#No more free space! You have 17 more cubes.

print(fill_the_box(10, 10,
10, 40, "Finish", 2, 15,
30))
#There is free space in the box. You could put 960 more cubes.
