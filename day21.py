# Program to access index of a list using for loop
# Start the indexing with non-zero value

my_list = [11,22,33,44]

# for index,value in enumerate(my_list,start=1):
#     print(index,value)
print(list(enumerate(my_list)))