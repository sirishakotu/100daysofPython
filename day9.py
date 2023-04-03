'''
Program to remove punctuation from a string

'''
punctuations = "''''!@#$%^&*()_+,."
string1 = input("Enter the input string:")
new_str = ""
for c in string1:
    if c not in punctuations:
        new_str+=c
print("New string:",new_str)