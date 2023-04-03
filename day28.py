# Count the occurences of each word in a given sentence

# given_string = input("Enter the string:")

# def word_count(string):
#     counts = dict()
#     words = string.split() # ==> here string converts into list
#     for each in words:
#         if each in counts:
#             counts[each] += 1
#         else:
#             counts[each] = 1
#     return counts

# print(word_count(given_string))

# Check if the key is already present in the dictionary

my_dict = {'a':1,'b':2,'c':3}
print(my_dict.keys())
print("Yes,its Present" if 'c' in my_dict.keys() else "Not there")