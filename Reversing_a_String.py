""" This program takes a string from the user and returns the reversed string """

def rev(a):
    new = ''
    index = len(a)

    while index:
        index -= 1
        new += a[index]
    return new

print(rev(a))

""" Alternate Method 2 """

def rev2(str):
    return ''.join(reversed(str))

print(rev2('Hi There'))

""" Alternate Method 3 """

def rev3():
    a = 'Sample String'
    print(a.[::-1])

rev3()

