text = input("Enter a string: ")

rev = ""

for ch in text:
    rev = ch + rev

if text == rev:
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")