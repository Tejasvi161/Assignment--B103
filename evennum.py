def even_numbers(numbers):
    even = []

    for i in numbers:
        if i % 2 == 0:
            even.append(i)

    return even

numbers = [10, 15, 20, 25, 30, 35]

result = even_numbers(numbers)

print("Even numbers:", result)
