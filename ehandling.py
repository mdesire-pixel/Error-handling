#print(10/0)
try:   
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number:"))
    result = num1/num2
except ZeroDivisionError:
    print("You cant divide by zero")
else:
    print(f"The answer is {result}")
    print("This will only execute if there is no exception")
