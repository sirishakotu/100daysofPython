# Program to triple all the numbers of a given list of integers using map 

# numbers = (1,2,3,4,5,6,7,8) # We can give any input,either list or tuple
# result = list(map(lambda x: x + x + x,numbers))
# print("Triple all the numbers of a given list of integers using map:",result)

# Program to write all the numbers that are divisble by 7 but not by 5

# for i in range(1,100):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i,end = " ")

# Program to write number of upper case and lower case letters in a string

given_string = input("Enter the input string:")
def string_test(string):
    d = {'UpperCase':0,'LowerCase':0}
    for i in  string:
        if i.isupper():
            d['UpperCase'] += 1
        elif i.islower():
            d['LowerCase'] += 1
        else:
            pass
    print("Number of Uppercase letters:",d['UpperCase'])
    print("Number of Lowercase letters:",d['LowerCase'])

string_test(given_string)
