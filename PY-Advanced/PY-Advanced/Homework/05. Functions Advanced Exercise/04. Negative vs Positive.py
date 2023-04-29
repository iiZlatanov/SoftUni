numbers = [int(el) for el in input().split()]
sum_of_negative = sum([number for number in numbers if number < 0])
sum_of_positive = sum([number for number in numbers if number > 0])

print(f"{sum_of_negative}\n{sum_of_positive}")

if abs(sum_of_negative) > sum_of_positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
