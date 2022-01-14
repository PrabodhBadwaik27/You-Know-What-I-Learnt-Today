'''
Problem: Check if prime number. Justify.
Input: Integer
Output: Boolean, String

Sol.:
    num%num, num%1 == 0
    num%x != 0

    1. input - n #check for integer
    2. traversal loop (2, n**0.5) and get remainder
        if remainder==0, for x, print(divisible by x) return false
        if not, return True
'''
def isPrime(num):
    if num==1:
        print("1 is a non-prime number.")
        return False
    if num%2==0:
        print("{} is divisible by 2. Hence, not a prime number.".format(num))
        return False
    div = int(num**0.5)
    for i in range(3, div+1, 2):
        if num%i==0:
            print("{} is divisible by {}. Hence, not a prime number.".format(num, i))
            return False
    print("{} is a prime number".format(num))
    return True

if __name__ == "__main__":
    try:
        num = int(input("Enter integer: "))
    except ValueError:
        num = int(input("Dirty input. Enter valid integer: "))

    isPrime(num)
