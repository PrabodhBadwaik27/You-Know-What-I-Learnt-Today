'''
Problem: Given an year, find if it is leap
Data: Input: Integer; Output: Boolean

Sol.:
    Conditions:
        1. %4=0
        2. %100!=0
        3. %400=0
'''

def leapYear(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            return False
        return True
    return False
    '''
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False
    '''
while True:
    try:
        year = int(input("Enter year: "))
        break
    except ValueError:
        print("Give a valid year input.")

print("{} is a leap year: {}".format(year, leapYear(year)))
