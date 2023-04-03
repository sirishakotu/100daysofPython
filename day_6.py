# 100daysofcode Challenge Day-6

# Program to find whether the string is palindrome or not?

string = input("Enter the string:")
str_1 = string.lower()
final = []
for each in str_1:
    final.append(each)
a = final[::-1]
b = ''.join(a)
if str_1 == str(b):
    print("The given string",string,"is palindrome string")
else:
    print("The given string",string,"is not palindrome string")