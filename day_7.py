'''
Write a python function to sum all the numbers in a list.

'''

list_1 = [12,15,85,23,65]
# print(sum([i for i in list_1]))  # list comprehension method

total = 0
for each in list_1:
    total += each
print("Sum of all numbers in a list:",total)