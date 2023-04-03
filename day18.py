## Accept hyphen seperated words as input

## Print the sorted words
'''
input:green-red-black-white
output:black-green-red-white
'''

# items = [n for n in input("Enter the String:").split("-")]
# items.sort()
# print("-".join(items))

l = ["green","red","black","white"]
l.sort()
print("-".join(l))