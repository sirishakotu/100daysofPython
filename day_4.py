# Challenge 100 Days Code Challenge Day 4

#Find the number is prime number or not?

def isprime(number):
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                return "Not a Prime"
        else:
            return "Prime"
    else:
        return "Not a Prime"

number = int(input("Enter the number:"))
print(isprime(number))

# a = 'Yog' * 2 * 3
# print(a)