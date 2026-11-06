str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("The strings are Anagrams")
else:
    print("The strings are not Anagrams")