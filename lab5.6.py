a = [2,3,4,5,6,7,8]
b = [10,9,8,7,5,3]
c = [3,7,2,4,6,2]
def sortedList(l):
    l1 = sorted(l)
    l2 = sorted(l, reverse = True)
    return (l == l1) or (l == l2)
print(sortedList(a))
print(sortedList(b))
print(sortedList(c))
