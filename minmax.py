numbers = [10, 25, 5, 40, 15]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest element:", largest)
print("Smallest element:", smallest)