# This program prints numbers present in both list1 and list2
def CommonList():
    list1 = [2,1,2,3,4,5]
    list2 = [2,3,4,7,8,9]
    new = []

    for i in list1:
        if i in list2:
            new.append(i)

    s = set(new)    # A set contains a list of elements with no repeated values
    print(s)
    print(new)

CommonList()
