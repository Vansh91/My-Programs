"""This program creates a list of all the numbers""" 
"""that can divide a number provided by the user"""

def NumberDivisibility():
    num = int(input("Enter a number:"))
    a = []
    for x in range(num + 1):
        if num % x == 0:
            a.append(x):
    print(a)

NumberDivisibility()
            
