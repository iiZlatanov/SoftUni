nums = [int(x) for x in input().split()]
positive_sum = sum(num for num in nums if num > 0)
negative_sum = sum(num for num in nums if num < 0)

print(f"{negative_sum}\n{positive_sum}")
if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
