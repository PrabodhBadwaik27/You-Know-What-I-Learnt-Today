'''
Problem: Given a number, check if it's an Armstrong number
Data:
    Input: Integer
    Output: Boolean
'''
def ArmstrongCheck(num):
    # variables: num, residue, rem; new(b)
    # eg = 303 {0:[,303, 0], 1:[3, 30, 3], 2:[0, 3, 30], 3:[303]}
    res = num #303
    b = 0 #0
    while res//10>0:
        rem = res%10
        res = res//10
        b = b*10 + rem
    b = b*10 + res%10
    print(num, b)
    return num==b


if __name__=="__main__":
    print("=========== Check if Given Integer is Armstrong Number ===========")
    while True:
        try:
            a = int(input("Enter a number: "))
            break
        except ValueError:
            print("Received dirty input. Enter a valid integer.", end=" ")
    print("{} is an Armstrong number: {}".format(a, ArmstrongCheck(a)))
