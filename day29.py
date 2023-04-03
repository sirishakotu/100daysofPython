# Program of recursion list sum
def recursion(data):
    total = 0
    for each in data:
        if type(each) == type([]):
            total += recursion(each)
        else:
            total += each
    return total

data = [[1,2],[3,4],[5,6],[7,8]]
print("Sum of all the data in list:",recursion(data))