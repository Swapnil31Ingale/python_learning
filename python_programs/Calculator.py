#This is test python calculator

#Take Inputs from user as 2 numbers 

print("Please enter the first number: ")
num1 = int(input())
print("Please enter the second number: ")
num2 = int(input())
#print(num1, num2)

print("Please select the operation: ")
print("1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division")
operation = int(input())
if operation == 1:
    print("Addition of", num1, "+", num2, "=", num1 + num2)
elif operation == 2:
    print("Subtraction of", num1, "-", num2, "=", num1 - num2)
elif operation == 3:
    print("Multiplication of", num1, "+", num2, "=", num1 * num2)
elif operation == 4:
    print("Division of", num1, "+", num2, "=", num1 / num2)
else:
    print("Please enter the valid operation")


