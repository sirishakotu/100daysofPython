# 100daysofcode Challenge Day-5

# Find the number is Armstrong or not without using power function

number = int(input("Enter the number:"))
length = len(str(number))
final = number
total = 0
while number != 0:
    a = number % 10
    total += (a ** length)
    number = number // 10
if total == final:
    print("The given number",final,"is Armstrong number")
else:
    print("The given number",final,"is not Armstrong number")


