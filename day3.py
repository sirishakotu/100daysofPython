## Challenge Day 3 ## 

# Program to compute all the permutations of the string

'''
1.if condition prints string passed as argument if it is equal to the length of string
2. In each iteration of the for loop, each character of string is stored in words.
3.The elements of words are swapped. 
  In this way, we achieve all different combinations of characters.
4. This process continues until the maximum length is reached.

'''

string = input("Enter the Input string:")

def permutation(string,i=0):
    if i == len(string):
        print(''.join(string))
    for j in range(i,len(string)):
        words = [c for c in string]
        words[i],words[j] = words[j],words[i] # swapping done here
        permutation(words,i+1)
permutation(string)

