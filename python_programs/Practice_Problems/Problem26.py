# Write a program that can find the factorial of a given number 
# provided by the user.

n = int(input("Number: "))
result = 1

for i in range(1, n+1):
    result = result * i
print(f"Factorial of {n} is {result}")