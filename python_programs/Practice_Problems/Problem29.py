# Print all the armstrong numbers in the range of 100 to 1000


num = int(input("Please enter a number: "))

a = num % 10 
b = num // 10
c = b % 10
d = b // 10

l = [a, c, d]
length = len(l)
def is_armstrong(num):
    if num < 100 or num > 1000:
        print("Please enter a number between 100 and 1000")
    else:
        if num == (l[0]) ** length + (l[1]) ** length + (l[2]) ** length:
            print(f"{num} is armstrong number")
        else:
            print(f"{num} is not armstrong number")
 
is_armstrong(num)      


# num = int(input("Please enter a number: "))

# # Splitting the digits of the input number
# digits = [int(digit) for digit in str(num)]

# def is_armstrong(num):
#     if num < 10:
#         print("Please enter a number greater than or equal to 10")
#     else:
#         num_digits = len(digits)
        
#         # Checking if the number is an Armstrong number
#         if num == sum(digit ** num_digits for digit in digits):
#             print(f"{num} is an Armstrong number")
#         else:
#             print(f"{num} is not an Armstrong number")

# is_armstrong(num)


        



