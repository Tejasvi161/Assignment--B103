numbers = [10, 20, 30, 20, 40, 10, 50]

new_list = []

for i in numbers:
    if i not in new_list:
        new_list.append(i)

print("List after removing duplicates:", new_list)