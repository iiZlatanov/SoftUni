# result = [abs(float(number)) for number in input().split()]
# print(result)

def absolute_values(list_1: list):
    result = [abs(float(number)) for number in list_1]
    return result


data = input().split(" ")
print(absolute_values(data))
