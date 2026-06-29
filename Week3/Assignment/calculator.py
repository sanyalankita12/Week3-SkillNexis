class Calculator:
    #Function for addition
    def add(self, a, b):
        return a + b

    #Function for Subtraction
    def subtract(self, a, b):
        return a - b

    #Function for multiplication
    def multiply(self, a, b):
        return a * b

    #Function for division
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"


calc = Calculator()

print(calc.add(10,5))
print(calc.subtract(10,5))
print(calc.multiply(10,5))
print(calc.divide(10,5))
print(calc.divide(10,0))
