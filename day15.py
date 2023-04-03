# Program to detect the number of local variables in a function

def Siri():
    x = 23
    y = 3.5
    z = "Spandana"
    a = 4
    b = "Rithwik"
print(Siri.__code__.co_nlocals)