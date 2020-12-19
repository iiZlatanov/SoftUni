n = int(input())
positives = []
negatives = []

for nums in range(n):
    read_a_number = int(input())
    if read_a_number < 0:
        negatives.append(read_a_number)
    else:
        positives.append(read_a_number)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}")