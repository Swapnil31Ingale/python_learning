# Write a program that will swap numbers

a = int(input("Enter the 3 digits number: "))

b = a % 10
c = a // 10
d = c % 10
e = c // 10

# print(a, b, c, d, e)

print(''.join([str(d), str(b), str(e)]))


# # Function to swap digits of a three-digit number
# def swap_digits(number):
#     if 99 < number < 1000:
#         digit1 = number // 100
#         digit2 = (number % 100) // 10
#         digit3 = number % 10

#         swapped_number = digit2 * 100 + digit1 * 10 + digit3
#         print(f"Before swapping: {number}")
#         print(f"After swapping: {swapped_number}")
#     else:
#         print("Please enter a valid three-digit number.")

# # Input a three-digit number from the user
# num = int(input("Enter a three-digit number: "))

# # Call the swap_digits function with the input number
# swap_digits(num)

