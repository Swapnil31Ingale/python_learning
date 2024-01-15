# Write a program that will take three digits from the user 
# and add the square of each digit.

#123 = 1*1 + 2*2 + 3*3 = 14

a = int(input("Please enter 3 digit no: "))

last_digit = a % 10
b = a // 10
second_digit = b % 10
first_digit = b // 10

sum = ((last_digit**2) + (first_digit**2) + (second_digit**2))
print(f"Sum of square of three digits {a} is {sum}.")