'''
Problem: Find factorial of the given (non-negative) integer.
Data:
    Input: Non-negative Integer [0, in)
    Output: Positive Integer [1, in)

Sol.:
    1. for num-->1: fact = fact*num
    2. if num==0: 0! = 1
'''
def factorialWithRecursion(num):
    if num==0:
        return 1
    else:
        return num*factorialWithRecursion(num-1)

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num<0:
                raise ValueError
            break
        except:
            num = print("Invalid input.", end=" ")
    print(factorialWithRecursion(num))