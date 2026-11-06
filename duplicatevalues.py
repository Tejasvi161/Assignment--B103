numbers = [10, 20, 30, 20, 40, 10, 50]

duplicates = []

for i in numbers:
    if numbers.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicate values:", duplicates)