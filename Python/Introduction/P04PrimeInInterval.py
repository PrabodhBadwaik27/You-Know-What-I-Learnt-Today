'''
Problem: Given two integers, we need to find all the prime numbers existing in that interval.

Data:
Input: 2 integer nos.
Output: List of integers

Sol:
1. traverse between lower bound, higher bound
2. For each number, check if it is prime
/*
2. [11, 28]: [11, 13, 15, 17, 19, 21, 23, 25, 27]
    {
        11: [3,],
        13: [3,],
        15: [3,],
        17: [3, 4],
        19: [3, 4]
    }
    [3, 3, 3, 4, 4]
    {
        3: [11, 13, 15, 17, 19, 21, 23, 25, 27],
        #4: [17, 19, 21, 23, 25, 27],
        5: [25, 27]
    }
*/
'''
def isPrime(num):
    for x in range(3, int(num**0.5)+1, 2):
        if num%x==0:
            return False
    return True


if __name__ == "__main__":
    primes = []
    interval = input("Enter inclusive range of integers (e.g. 3 73): ").split(" ")
    while True:
        try:
            a = int(interval[0])
            b = int(interval[1])
            break
        except:
            interval = input("Invalid input. Re-enter inclusive range of integers (e.g. 3 73): ").split(" ")

    if a<=2:
        primes.append(2)
        a = 3
    elif a%2==0:
        a = a+1
    for i in range(a, b, 2):
        if isPrime(i):
            primes.append(i)

    print(primes)