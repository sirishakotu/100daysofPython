# Program to add 2 matrices using nested loops

X = [[12,9,3],[4,5,6,],[7,8,3]]
y = [[9,8,1],[6,7,3],[4,5,9]]
result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j]=X[i][j] + y[i][j]
for r in result:
    print(r)