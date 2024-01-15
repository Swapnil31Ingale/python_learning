# Write a program that will check whether the number is armstrong 
# number or not.

# 153
# 1**3 + 5**3 + 3**3 = 153

num = int(input("Enter the number: "))

a = num % 10
b = num // 10
c = b % 10
d = b // 10

if (a**3) + (c**3) + (d**3) == num:
    print(f"{num} is Armstrong number.")
else:
    print(f"{num} is not Armstrong number.")
    