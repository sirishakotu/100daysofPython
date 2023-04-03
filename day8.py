'''
Add two given lists using map and lambda

'''
l1 = [23,5,45]
l2 = [56,21,32]
total = map(lambda x,y:x+y,l1,l2)
print("The total of two given lists:",list(total))