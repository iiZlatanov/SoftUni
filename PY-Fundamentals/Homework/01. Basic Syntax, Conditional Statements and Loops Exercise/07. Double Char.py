command = input()
while command != "End":
    result_command = ""
    for ch in command:
        result_command += ch * 2

    if result_command != "SSooffttUUnnii":
        print(result_command)

    command = input()
