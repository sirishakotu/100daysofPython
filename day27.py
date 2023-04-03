# Calculate the length of the string

string = input("Enter the string:")
# print("Length of the string",string,"is",len(string))
def string_length(string):
    count = 0
    for i in string:
        count += 1
    return count
print("Length of the string",string,"is",string_length(string))