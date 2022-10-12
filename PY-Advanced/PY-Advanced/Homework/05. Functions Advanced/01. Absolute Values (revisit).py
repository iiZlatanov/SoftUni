def turn_into_absolute_values(nums_list):
    result = [abs(el) for el in nums_list]
    return result


nums = [float(el) for el in input().split()]
print(turn_into_absolute_values(nums))
