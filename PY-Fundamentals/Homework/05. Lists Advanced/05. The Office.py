def convert_to_int(el):
    return int(el)


nums_as_strings = ["1", "2", "3"]

nums = list(map(convert_to_int, nums_as_strings))
print(nums)
