number = int(input())
counter = 0

for i in range(1, number):
    if number % i == 0:
        counter += i

if counter == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")