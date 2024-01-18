# Write a program to find the sum of first n numbers, 
# where n will be provided by the user. Eg if the user 
# provides n=10 the output should be 55.

n = int(input("Enter the number: "))

sum = 0

for i in range(0 ,n+1):
    sum = sum + i
    i = i + 1
print(f"Sum of first {n} numbers is {sum}.")
    
