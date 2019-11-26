"""This program taks an input from the user and checks to see,"""
"""if it's in the given sorted list using binary search."""

list1 = [3,10,17,35,45,60]

def checking_number():
    a = int(input('Enter the number'))
    return a

def binary_search():
    num_to_search = checking_number()

    first = 0
    last = len(list1)
    found = False

    while(first <= last and not found):
        mid = (first + last)/2
        if(num_to_search == list1[mid]):
            found = True
            print('Found it!')
        elif(num_to_Search < list1[mid]):
            last = mid - 1
            found = True
            print('Found below')
        else:
            first = mid + 1
            found = True
            print('Found higer')
        if(found == False):
            print('Not in list')

binary_search()

        
