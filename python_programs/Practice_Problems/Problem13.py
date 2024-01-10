# Write  a program that will tell whether the given number is divisible by 3 & 6.

a = int(input("Number: "))

if a % 3 == 0 and a % 6 == 0:
    print("Number divisible by 3 and 6")
else:
    print("Number is not divisible by 3 and 6")