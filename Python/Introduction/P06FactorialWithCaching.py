class Factorial:
    cache = {0: 1}

    def calculateFact(self, num):
        if num not in self.cache:
            self.cache[num] = num * self.calculateFact(num-1)
        return self.cache[num]


if __name__ == "__main__":
        while True:
            try:
                num = int(input("Enter a non-negative integer: "))
                if num<0:
                    raise ValueError
                break
            except:
                print("Invalid input.", end=" ")

        a = Factorial()
        print(a.calculateFact(num))
        print(a.cache)