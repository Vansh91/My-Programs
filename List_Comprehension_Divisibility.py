# This program displays all the even numbers from a list using list comprehension.

def Divisibility():
    a = [1,4,9,16,25,36,49,64,81,100]
    b = [i for i in a if i%2 == 0]

    print(b)

Divisibility()
