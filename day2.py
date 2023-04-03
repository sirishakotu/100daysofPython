## Challenge Day 2 ##

# 1. Find the largest among 3 input numbers

list_numbers = [14,12,25]

''' Solution 1'''
# max_list = max(list_numbers)
# print("The Maximum number in the list:",max_list)

'''Output: The Maximum number in the list: 25'''

''' Solution 2'''
# max_number = list_numbers[0]
# for each in list_numbers:
#     if each > max_number:
#         max_number = each
# print("The Maximum number in the list:",max_number)

''' Solution 3 '''
# list_numbers.sort(reverse=True)
# print("The Maximum number in the list:",list_numbers[0])