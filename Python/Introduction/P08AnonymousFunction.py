'''
    Problem: Display Powers of 2 Using Anonymous Function
    Data:
        Input: Integer (n)
        Output: Integer (result)
    Value: Anonymous/ Lambda functions
'''
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter an integer: "))
            break;
        except ValueError:
            print("Invalid input. Try again.")
    print("{}th power of 2 is {}".format(n, (lambda i: 2**i)(n)))

