m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))
m4 = int(input("Enter marks for subject 4: "))
m5 = int(input("Enter marks for subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage)

if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
    print("Result: Pass")

    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 75:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C")
    elif percentage >= 35:
        print("Grade: D")
else:
    print("Result: Fail")
    print("Grade: F")