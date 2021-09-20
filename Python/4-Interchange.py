# Python Program to Interchange 'first' and 'last' elements in a List
def Interchange(lst):
    temp = lst[0]
    last = len(lst)-1
    lst[0] = lst[last]
    lst[last] = temp
    return lst     

lst = [1,2,3,4,5]
print(Interchange(lst))    
