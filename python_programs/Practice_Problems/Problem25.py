# Write a program that can multiply 2 numbers provided by the user 
# without using the * operator

n1 = int(input("First number: "))
n2 = int(input("Second number: "))

def multiply(n1, n2):
    result = 0
    for i in range(n2):
        result = result + n1
    return result

print("Multiplication: ", multiply(n1, n2))
