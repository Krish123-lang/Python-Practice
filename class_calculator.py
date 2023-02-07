# Class Calculator

class Calc:
    def __init__(self, a, b) -> None: # Constructor
        self.a = a
        self.b = b

    def summ(self):
        print(f"The sum: {self.a} + {self.b} is {self.a+self.b}\n") # Sum

    def difference(self):
        print(f"The difference: {self.a} - {self.b} is {self.a-self.b}\n") # Difference

    def multiplication(self):
        print(f"The multiplication: {self.a} * {self.b} is {self.a*self.b}\n") # Multiplication

    def divison(self):
        print(f"The divison: {self.a} / {self.b} is {self.a/self.b}\n") # Divide

try:
    while True:
        """ Accepting input """

        a = int(input("Enter first number: ")) 
        b = int(input("Enter second number: "))

        sum1 = Calc(a, b)
        sum1.summ()

        difference1 = Calc(a, b)
        difference1.difference()

        multiple1 = Calc(a, b)
        multiple1.multiplication()

        divide1 = Calc(a, b)
        divide1.divison()

except Exception as e:
    print(e)
