# Python Program for Sum of Squares of First n Natural numbers
def SumOfSquares(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i*i
    return sum

print(SumOfSquares(4))
