def rounding(nums_list):
    result = [round(el) for el in nums_list]
    return result


nums = [float(el) for el in input().split()]
print(rounding(nums))
