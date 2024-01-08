# User will input (2numbers).Write a program to swap the numbers
no_1 = int(input("No One: "))
no_2 = int(input("No Two: "))

temp_var = no_1
no_1 = no_2
no_2 = temp_var


print(f"After swapping, No 1 is {no_1} and No 2 is {no_2}.")