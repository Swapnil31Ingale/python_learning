# Write a program that will give you the sum of 3 digits

sum = 0
no = int(input("Number is: "))
a = no % 10 #(791 % 10 = 1)
no = no // 10 #(791 // 10 = 79)
b = no % 10 #(79 % 10 = 9)
c = no // 10 #(79 // 10 = 7)

sum = a + b + c
print(f"Sum of 3 digits is {sum}.")


# Wrong Answer
# digit = []

# for i in range(3):
#     user_input = int(input("Enter the number: "))
#     digit.append(user_input)
#     sum += digit[i]
# print(f"Sum of 3 digits is {sum}.")
    