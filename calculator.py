print("-------------Calculator-------------")
print("Select the number of the desired operation: ")
print(" 1 - Addition \n 2 - Subtraction \n 3 - Multiplication \n 4 - Division")
operator = input("Enter the operator: ")
value1 = int(input("Enter value 1: "))
value2 = int(input("Enter value 2: "))

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

if operator == "+":
    print("The sum of " + str(value1) + " plus " + str(value2) + " is equal to: ", add(value1, value2))
elif operator == "-":
    print("The subtraction of " + str(value1) + " minus " + str(value2) + " is equal to: ", subtract(value1, value2))
elif operator == "*":
    print("The multiplication of " + str(value1) + " times " + str(value2) + " is equal to: ", multiply(value1, value2))
elif operator == "/":
    print("The division of " + str(value1) + " by " + str(value2) + " is equal to: ", divide(value1, value2))
