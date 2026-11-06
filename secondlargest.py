numbers = [10, 25, 30, 40, 15]

largest = second_largest = float('-inf')

for i in numbers:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print("Second largest number:", second_largest)
