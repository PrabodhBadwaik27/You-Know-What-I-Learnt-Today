print("Quadratic equations are the polynomial equations of the form ax^2+bx+c=0.\n"
      "We will find the valid solutions for any given quadratic equation in this program.")

a, b, c = (int(i) for i in input("Enter coefficients a, b, c: ").split(" "))

x1 = -b - ((b**2 - 4*a*c)**0.5)/2*a
x2 = -b + ((b**2 - 4*a*c)**0.5)/2*a

print("Quadratic Equation: ({})x^2+({})x+({})=0".format(a, b, c))
print("Solution: {}, {}".format(x1, x2))